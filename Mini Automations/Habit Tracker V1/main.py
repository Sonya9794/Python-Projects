import time

import actions
import infrastructure
import habit_statistics

exit_loop = False

print("Hello! What would you like to do?\n")
time.sleep(0.5)

while not exit_loop:
    print("A. Create a new habit")
    time.sleep(0.1)
    print("B. Delete a habit")
    time.sleep(0.1)
    print("C. Log a completed habit for today")
    time.sleep(0.1)
    print("D. View list of current habits")
    time.sleep(0.1)
    print("E. See statistics")
    time.sleep(0.1)
    print("F. Exit")
    time.sleep(0.5)

    requested_action = input("\nType the letter corresponding to your desired action: ").strip().lower()

    if requested_action == 'a':
        actions.add_habit()
    elif requested_action == 'b':
        actions.delete_habit()
    elif requested_action == 'c':
        print("Here's your list of habits:")
        infrastructure.print_habit_list()
        print("Other (enter name below)")
        completed_habit = input("Which of your habits did you complete?: ").strip().lower()
        actions.log_today(completed_habit)
    elif requested_action == 'd':
        print("Here's your list of habits:")
        infrastructure.print_habit_list()
    elif requested_action == 'e':
        habit_statistics.streaks()

    requested_action = input("Exit (Y/N)?: ").strip().lower()

    if requested_action == 'y':
        exit_loop = True
    else:
        time.sleep(0.5)
        print("\nWhat would you like to do next?\n")
        time.sleep(0.5)