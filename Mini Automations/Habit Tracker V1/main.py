import time

import actions
import infrastructure

exit = False

while not exit:
    print("A. Create a new habit")
    print("B. Log a completed habit for today")
    print("C. View current habits")
    print("D. See statistics")
    print("E. Exit")

    requested_action = input("Type the letter corresponding to your desired action: ").strip().lower()

    if requested_action == 'a':
        actions.add_habit()
    elif requested_action == 'b':
        print("Here's your list of habits:")
        infrastructure.print_habit_list()
        print("Other (enter name below)")
        completed_habit = input("Which of your habits did you complete?: ").strip().lower()

        actions.log_today(completed_habit)

    exit = True