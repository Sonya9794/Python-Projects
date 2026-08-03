import os
import time

habits_list_path = os.path.join(os.path.dirname(__file__), 'habits_list.txt')
habits_data_path = os.path.join(os.path.dirname(__file__), 'habits_data.txt')

def check_files_exist():
    if not os.path.exists(habits_list_path):
        with open(habits_list_path, 'x'):
            None
    if not os.path.exists(habits_data_path):
        with open(habits_data_path, 'x'):
            None


def print_habit_list():
    with open (habits_list_path) as habits_list:
        for line in habits_list:
            if line != "\n":
                print(line.strip().capitalize())
                time.sleep(0.1)


def uniqueness(input):
    unique = True
    with open (habits_list_path) as habits_list:
        for line in habits_list:
            if line.strip().lower() == input.strip().lower():
                unique = False
    return unique

"""def split_line(line_number):
    with open(habits_data_path) as habits_data:
        for i, line in enumerate(habits_data):
            if i == int(line_number.strip().lower()):
                data = line.split("|")
                return data"""



def get_last_line():
    with open(habits_data_path) as habits_data:
        last_line = habits_data.readlines()[-1].strip().lower()
    return last_line

def get_last_date():
    latest_date = get_last_line().split("|")[0]
    return latest_date.lstrip().lower()