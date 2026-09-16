
from random import random

def get_color():
    value = random() * 100
    if value <= 3:
        return 2
    elif value <= 51.5:
        return 0
    else:
        return 1

def start_game():
    user_bilance = 1_000
    print("Welcome to casino Royal")
    while True:
        bet = int(input(f"Select your bet ({user_bilance}eur): "))
        while bet > user_bilance or bet <= 0:
            if bet <= 0:
                print("Sázka musí být větší než 0.")
            else:
                print("Dej min (nemáš dost peněz)")
            bet = int(input(f"Select your bet ({user_bilance}eur): "))
       
        print("Select color:")
        print("\t\t0 - Red")   # 48.5%
        print("\t\t1 - White") # 48.5%
        print("\t\t2 - Green") # 3%
        print("\t\t4 - leave game")
       
        selection = int(input("Select: "))
       
        while selection > 4 or selection < 0:
            print("Neplatná volba, zkus to znovu.")
            selection = int(input("Select: "))

        if selection == 4:
            return
       
        if selection == get_color():
            user_bilance += bet
            print("You won!!")
        else:
            user_bilance -= bet
            print(f"You lost {bet}eur")

        if user_bilance <= 0:
            print("Došly ti peníze! Konec hry.")
            break

if __name__ == "__main__":
    start_game()