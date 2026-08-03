import datetime
import os
import time

import infrastructure

habit_list_path = os.path.join(os.path.dirname(__file__), 'habits_list.txt')
habit_data_path = os.path.join(os.path.dirname(__file__), 'habits_data.txt')

def streaks():
    longest_streak = 0
    longest_habit = "None"

    current_date = datetime.date.today()
    previous_date = datetime.date.today()

    done_today = False

    print("\nHere are your current streaks for each of your goals!")
    time.sleep(0.5)
    print()

    with open(habit_list_path) as habit_list:
        habits = habit_list.read().splitlines()


    with open(habit_data_path) as habit_data:
        raw_data = habit_data.read().splitlines()

        for habit in habits:
            current_streak = 0
            data_lines = raw_data
            done_today = False

            if infrastructure.get_last_date() == str(current_date):
                if habit in infrastructure.get_last_line():
                    done_today = True
                
                data_lines.pop()


            for data_line in reversed(data_lines):
                data = data_line.split("|")

                previous_date = data[0]

                previous_date = datetime.date.fromisoformat(previous_date)
                difference = current_date - previous_date
                current_date = previous_date

                if habit.strip() in data and difference.days == 1:
                    current_streak += 1

                elif habit.strip() in data:
                    current_streak += 1
                    break
                    
                else:
                    break

            if done_today == True:
                current_streak += 1
                message = "(done today)"
            else:
                message = "(not done today)"

            if longest_streak < current_streak:
                longest_streak = current_streak
                longest_habit = habit
                
            print(f"{habit.capitalize()} every day: {current_streak} days in a row {message}.")
            time.sleep(0.1)

        time.sleep(0.4)
        print(f"\nYour longest commitment has been to {longest_habit}, which you've done for {longest_streak} days!")
        time.sleep(0.5)

        



                
