if __name__ == "__main__":
    str_time = input("Zadej cas v S:")
    time = int(str_time)
    hour = time // 3600
    minuty = (time % 3600) // 60
    sekundy = (time % 3600) % 60
    print(f"{hour}:{minuty}:{sekundy}")