import argparse
import json

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
        substitute_method = input("Enter the substitute method (average, weighted_average, max, min, median): ")
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

    print("\nHomework List:")
    for homework in homework_manager.homework_list:
        print(f"Name: {homework['Name']}")
        # print(f"ID: {homework['ID']}")
        print(f"Substitute Method: {homework['Substitute Method']}")
        print(f"Substitute Assignments: {homework['Substitute Assignments']}")


