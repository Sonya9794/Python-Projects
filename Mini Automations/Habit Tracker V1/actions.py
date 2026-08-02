import datetime
import os
import time

import infrastructure

habit_list_path = os.path.join(os.path.dirname(__file__), 'habits_list.txt')
habit_data_path = os.path.join(os.path.dirname(__file__), 'habits_data.txt')

def add_habit():
    exit = False

    while not exit:
        habit_name = input("What habit would you like to create?: ").strip().lower()

        if infrastructure.uniqueness(habit_name) == False:
            print("You are already tracking this habit!")
            time.sleep(0.5)
            try_again = input("Do you still want to add a habit (Y/N)?: ").strip().lower()

            if not try_again == 'y':
                exit = True
                print("Returning to menu.")
                time.sleep(0.5)

        else:
            with open(habit_list_path, 'a') as habit_list:
                habit_list.write(f"{habit_name}\n")
                print(f"{habit_name.capitalize()} has been added to your list of habits!")
                exit = True


def log_today(habit):

    habit = habit.strip().lower()

    date = datetime.date.today()

    if infrastructure.uniqueness(habit) == True:
        print("You are not currently tracking this habit.")
        time.sleep(0.5)
        add = input(f"Would you like to add \"{habit.strip().lower()}\" to your habits (Y/N)?").strip().lower()
        if add == 'y':
            add_habit(habit)

    elif habit in infrastructure.get_last_line().split("|") and str(infrastructure.get_last_date()) == str(date):
        print("This habit was already logged today!")

    else:
        if str(infrastructure.get_last_date()) == str(date):
            with open(habit_data_path, 'a') as habit_data:
                habit_data.write(f"|{habit.strip().lower()}")
        else:
            with open(habit_data_path, 'a') as habit_data:
                habit_data.write(f"\n{date}|{habit}")