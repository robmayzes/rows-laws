import random
import time
import sys

# Import laws from txt file

with open("Laws.txt") as all_laws:
    str_laws = all_laws.read()
    laws = str_laws.split('\n')
total_laws = len(laws)

# Get user prefs

def days_input():
    days = input("How many day's would you like to split the laws over?\n")
    try:
        integer = int(days)
        return integer
    except ValueError:
        print("\nPlease enter an integer. Let's try again...\n")
        return

def sleep_input():
    days = input("How long (in seconds) do you want to pause between each law?\n")
    try:
        integer = int(days)
        return integer
    except ValueError:
        print("\nPlease enter an integer. Let's try again...\n")
        return

# Show random laws function

def show_laws(days, sleep_time, int_laws_per_day):
    for day in range(days-1):
        print("\nOkay! Ready for your daily principles?")
        for today in range(int_laws_per_day):
            input("\n>>> Press enter to see the next law...\n")
            current_law = random.choice(laws)
            print(current_law)
            laws.remove(current_law)
            time.sleep(sleep_time)
        print("\nThat's it for today! Come back here tomorrow for the next round. "
                     "Or, would you prefer to quit? (y/n)\n")
        play_again()
    while len(laws) != 0:
        input("\n>>> Press enter to see the next law...\n")
        current_law = random.choice(laws)
        print(current_law)
        laws.remove(current_law)
        time.sleep(sleep_time)
    print("\nThat's all of the laws. See you next time!\n")

# User input functions

def sleep_f(days):
    sleep_time = sleep_input()
    if isinstance(sleep_time, int):
        laws_per_day = total_laws/days
        int_laws_per_day = int(laws_per_day)
        show_laws(days, sleep_time, int_laws_per_day)
    else: 
        sleep_f(days)

def days_f():
    days = days_input()
    if isinstance(days, int):
        sleep_f(days)
    else:
        days_f()

def play_again():
    play = input("")
    if play == "n":
        print("\nCool, see you tomorrow! \n\n---------------------------------\n")
        time.sleep(1) 
        # TODO: Change back to 600
        return
    elif play == "y":
        print("\nNo problem. See you later!")
        sys.exit()
    else:
        print("\n(Please enter y or n.)")
        play_again()

# Run program

def run():
    print('Welcome to Robs Laws. Total Laws = ' + str(total_laws))
    time.sleep(1)
    days_f()

run()