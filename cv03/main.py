def time_format():
    str_time = input("Zadej cas v S:")
    time = int(str_time)
    hour = time // 3600
    minuty = (time % 3600) // 60
    sekundy = (time % 3600) % 60
    print(f"{hour}:{minuty}:{sekundy}")

if __name__ == "__main__":
    value = int(input("Zadej castku:"))
    money = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    for item in money:
        x_money = value // item
        value = value - (x_money * item)
        print(f"{item}x {x_money}")