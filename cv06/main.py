def test_fun():
    i = 5
    j = 4
    return i, j

lst = {1, "Ahoj", None} # list
print(f"lst[0] -> {lst[0]}")
print(len(lst))
for item in lst:
    print(item)

lst.append(5) # prida 5 na konec listu
del lst[1] # smaze prvek na indexu 1

if 1 in lst:
    pass

lst[-1] = 5 # posledni prvek
i, j = test_fun()

tpl = (1, 2, 3) # tuple
print(f"tpl[0] -> {tpl[0]}")
print(len(tpl))
for item in tpl:
    print(item)

st = {1,2,1,3,1,2,1} # set
print(st[0])
print(len(st))
for item in st:
    print(item)

dct = {
    "key": "value",
    1 : 5
}