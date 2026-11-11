
import cv2
import numpy as np
import os
from tkinter import Tk, filedialog

# ==================================
# 1. VYBER SKEN
# ==================================

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Vyber naskenovaný papír",
    filetypes=[("Obrázky", "*.png *.jpg *.jpeg *.bmp")]
)

if not path:
    print("Nebyl vybrán obrázek!")
    exit()

image = cv2.imread(path)

if image is None:
    print("Obrázek se nepodařilo načíst!")
    exit()

print("Obrázek načten!")

# ==================================
# 2. ZADEJ ROZMĚRY TABULKY
# ==================================

rows = int(input("Kolik má tabulka řádků? "))
cols = int(input("Kolik má tabulka sloupců? "))

# ==================================
# 3. OZNAČ CELOU TABULKU
# ==================================

print("Myší označ celou tabulku a stiskni ENTER.")

x, y, w, h = cv2.selectROI(
    "Oznac celou tabulku",
    image,
    False,
    False
)

cv2.destroyAllWindows()

if w == 0 or h == 0:
    print("Tabulka nebyla označena!")
    exit()

table = image[y:y+h, x:x+w]

# ==================================
# 4. VYTVOŘ SLOŽKU
# ==================================

output = "cislice"
os.makedirs(output, exist_ok=True)

# ==================================
# 5. ROZDĚLENÍ TABULKY
# ==================================

counter = 0

cell_w = w / cols
cell_h = h / rows

for r in range(rows):
    for c in range(cols):

        # Souřadnice políčka
        x1 = int(c * cell_w)
        x2 = int((c + 1) * cell_w)

        y1 = int(r * cell_h)
        y2 = int((r + 1) * cell_h)

        cell = table[y1:y2, x1:x2]

        # Odstranění okrajů a čar tabulky
        margin_x = int(cell.shape[1] * 0.10)
        margin_y = int(cell.shape[0] * 0.10)

        cell = cell[
            margin_y:cell.shape[0]-margin_y,
            margin_x:cell.shape[1]-margin_x
        ]

        # ==================================
        # 6. ČERNOBÍLÝ OBRAZ
        # ==================================

        gray = cv2.cvtColor(
            cell,
            cv2.COLOR_BGR2GRAY
        )

        _, binary = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )

        # ==================================
        # 7. NALEZENÍ ČÍSLICE
        # ==================================

        points = cv2.findNonZero(binary)

        if points is None:
            print("Prázdné políčko:", r + 1, c + 1)
            continue

        bx, by, bw, bh = cv2.boundingRect(points)

        digit = binary[by:by+bh, bx:bx+bw]

        # ==================================
        # 8. ZMĚNA VELIKOSTI
        # ==================================

        scale = 200 / max(bw, bh)

        new_w = max(1, int(bw * scale))
        new_h = max(1, int(bh * scale))

        digit = cv2.resize(
            digit,
            (new_w, new_h),
            interpolation=cv2.INTER_AREA
        )

        # Bílé pozadí, černá číslice
        canvas = np.ones(
            (256, 256),
            dtype=np.uint8
        ) * 255

        px = (256 - new_w) // 2
        py = (256 - new_h) // 2

        canvas[
            py:py+new_h,
            px:px+new_w
        ] = 255 - digit

        # ==================================
        # 9. ULOŽENÍ
        # ==================================

        counter += 1

        filename = f"cislice_{counter}.png"

        cv2.imwrite(
            os.path.join(output, filename),
            canvas
        )

        print("Uloženo:", filename)

# ==================================
# 10. HOTOVO
# ==================================

print("==========================")
print("HOTOVO!")
print("Počet uložených číslic:", counter)
print("Rozměr: 256 x 256 px")
print("Složka:", output)
print("==========================")
