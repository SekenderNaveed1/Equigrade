import argparse
import json
import sys

def user_prompt(x, i):
    answer = 0
    while ((answer != " Yes") & (answer != "No")):
        if (i <= 1):
            answer = input("Do you want to change anything?")
        else: 
            answer = input("Do you want to change anything else?")
        if (answer == " Yes"):
            i = i + 1
            answer2 = 0
            while ((answer2 != " Name") & (answer2 != " Substitute Method") & (answer2 != " Substitute Assignment")):
                answer2 = input("What do you want to change?")
                if (answer2 == " Name"):
                    answer3 = input("What would you like the new name to be?")
                    x['Name'] = answer3 #This part isn't working because the name isn't actually being changed. 
                elif (answer2 == " Substitute Method"):
                    answer3 = 0
                    while ((answer3 != " average") & (answer3 != " weighted_average") & (answer3 != " max") & (answer3 != " min") & (answer3 != " median")):
                        answer3 = input("What would you like the new substitute method to be?")
                    x['Substitute Method'] = answer3 #This part isn't working because the substitute method isn't actually being changed.
                elif (answer2 == " Substitute Assignments"):
                    #Work on this part later. I need to ask how many assignments there are and accept that number of inputs. 
                    answer3 = input("What would you like the new substitute assignments to be?")
                    x['Substitute Assignment'] = answer3 #This part isn't working because the substitute assignments aren't actually being changed.
        elif (answer == " No"):
            sys.exit()

class EnvironmentSettings:
    def __init__(self):
        self.setting1 = None
        self.setting2 = None

    def set_setting(self, setting_name, value):
        if setting_name == 'setting1':
            self.setting1 = value
        elif setting_name == 'setting2':
            self.setting2 = value

class HomeworkManager:
    def __init__(self):
        self.homework_list = []

    def add_homework(self, name, substitute_method, substitute_assignments):
        homework_data = {
            "Name": name,
            # "ID": id,
            "Substitute Method": substitute_method,
            "Substitute Assignments": substitute_assignments
        }
        self.homework_list.append(homework_data)

    def print_homework_data(self):
        i = 0
        print("\nHomework List:")
        for homework in self.homework_list:
            print(f"Name: {homework['Name']}") # This part isn't working. It keeps printing the wrong name. 
            # print(f"ID: {homework['ID']}")
            print(f"Substitute Method: {homework['Substitute Method']}") # This line isn't working. It keeps saying the substitute method is "average" regardless of what I put in. 
            print(f"Substitute Assignments: {homework['Substitute Assignments']}") # This line isn't working. It keeps printing "Test Quiz", "Test Quiz 2", and "Test Quiz 3" regardless of what I put in. 
            i = i + 1
            user_prompt(homework, i)

def save_data(environment, homework_manager):
    data = {
        "environment": {
            "setting1": environment.setting1,
            "setting2": environment.setting2
        },
        "homework_list": homework_manager.homework_list
    }

    with open("data.json", "w") as data_file:
        json.dump(data, data_file)

def load_data():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = {
            "environment": {},
            "homework_list": []
        }
    return data

def get_substitute_assignments(number_of_substitute_assignments):
    substitute_assignments = []
    for i in range(int(number_of_sub_assignments)):
            substitute_assignments.append(input(f"Enter substitute assignment {i+1}: "))
    return substitute_assignments


if __name__ == "__main__":
    data = load_data()

    # Initialize EnvironmentSettings and HomeworkManager objects with loaded data
    environment = EnvironmentSettings()
    environment.setting1 = data["environment"].get("setting1")
    environment.setting2 = data["environment"].get("setting2")

    homework_manager = HomeworkManager()
    homework_manager.homework_list = data["homework_list"]

    # Create a parser object
    parser = argparse.ArgumentParser(description="Manage environment settings and homework")

    # Define command-line flags
    parser.add_argument("--setting1", help="Set the value of setting1")
    parser.add_argument("--setting2", help="Set the value of setting2")
    parser.add_argument("--add-homework", action="store_true", help="Add homework")

    # Parse command-line arguments
    args = parser.parse_args()

    # Set environment settings based on command-line flags
    if args.setting1:
        environment.set_setting("setting1", args.setting1)

    if args.setting2:
        environment.set_setting("setting2", args.setting2)

    # Perform actions based on command-line flags
    if args.add_homework:
        # Prompt the user for homework details
        name = input("Enter the name of the homework: ")
        substitute_method = 0
        while ((substitute_method != "average") & (substitute_method != "weighted_average") & (substitute_method != "max") & (substitute_method != "min") & (substitute_method != "median")):
            substitute_method = input("Enter the substitute method (average, weighted_average, max, min, median): ")
            if ((substitute_method == "average") | (substitute_method == "weighted_average") | (substitute_method == "max") | (substitute_method == "min") | (substitute_method == "median")):
                number_of_sub_assignments = input("Enter the number of assignments you want to use to calculate substitute grade: ")

        substitute_assignments = get_substitute_assignments(number_of_sub_assignments)
        
       

        # Add the homework with the provided details
        homework_manager.add_homework(name, substitute_method, substitute_assignments)

        # Save data immediately after adding a homework
        save_data(environment, homework_manager)

    # Print or manipulate the environment and homework data as needed
    print("Environment Settings:")
    print(f"Setting1: {environment.setting1}")
    print(f"Setting2: {environment.setting2}")

    homework_manager.print_homework_data()

