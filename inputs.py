import json
import numpy as np
from input_func import *
class Homework:
    def __init__(self, name, substitute_method, substitute_assignments):
        self.name = name
        self.substitute_method = substitute_method
        self.substitute_assignments = substitute_assignments

class HomeworkManager:
    def __init__(self):
        self.homework_list = []

    def add_homework(self, name, substitute_method, substitute_assignments):
        self.homework_list.append(Homework(name, substitute_method, substitute_assignments))

    def print_homework_data(self):
        for i, homework in enumerate(self.homework_list):
            print(f"\n    {i+1})\tName: {homework.name}")
            print(f"\tSubstitute Method: {homework.substitute_method}")
            print(f"\tSubstitute Assignments: {homework.substitute_assignments}")

    def validate_input(self):
        yes = ["Yes","yes","y","Y"]
        no = ["No","no","n","N"]
        while True:
            self.print_homework_data()
            answer = get_input(f"Do you want to change anything? (y/n): ", np.union1d(yes,no))
            if answer in no:
                break
            # asks user which assignment they would like to change
            index = int(get_int("Enter the index of the assignment you would like to change: ", len(self.homework_list))) - 1
            validate_homework(self.homework_list[index])
class EnvironmentSettings:
    def __init__(self, setting1=None, setting2=None):
        self.setting1 = setting1
        self.setting2 = setting2

def save_data(environment, homework_manager):
    data = {
        "environment": {
            "setting1": environment.setting1,
            "setting2": environment.setting2
        },
        "homework_list": [{"name": hw.name, "substitute_method": hw.substitute_method, "substitute_assignments": hw.substitute_assignments} for hw in homework_manager.homework_list]
    }
    with open("data.json", "w") as data_file:
        json.dump(data, data_file)

def load_data():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            environment = EnvironmentSettings(data["environment"]["setting1"], data["environment"]["setting2"])
            homework_manager = HomeworkManager()
            for hw_data in data["homework_list"]:
                homework_manager.add_homework(hw_data["name"], hw_data["substitute_method"], hw_data["substitute_assignments"])
            return environment, homework_manager
    except FileNotFoundError:
        return EnvironmentSettings(), HomeworkManager()


if __name__ == "__main__":
    environment, homework_manager = load_data()

    while True:
        action = get_input("What would you like to do? (add-homework/show-homework/quit) ", ["add-homework", "show-homework", "quit"])
        if action == "quit":
            break
        elif action == "add-homework":
            name = input("Enter the name of the homework: ").strip()
            substitute_method = get_input("Enter the substitute method (average/weighted_average/max/min/median): ", ["average", "weighted_average", "max", "min"])
            number_of_substitute_assignments = get_int("How many substitute assignments would you like?: ")
            substitute_assignments = get_substitute_assignments(number_of_substitute_assignments)
            homework_manager.add_homework(name, substitute_method, substitute_assignments)
            save_data(environment, homework_manager)
        elif action == "show-homework":
            homework_manager.validate_input()
