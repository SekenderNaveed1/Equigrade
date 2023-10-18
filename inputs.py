import argparse
import json
from sub_weighted_avg import sub_weighted_avg

class EnvironmentSettings:
    def __init__(self):
        self.setting1 = None

    def set_setting(self, setting_name, value):
        if setting_name == 'setting1':
            self.setting1 = value

class HomeworkManager:
    def __init__(self):
        self.homework_list = []

    def add_homework(self, name, score, weight):
        homework_data = {
            "Name": name,
            # "ID": id,
            "Score": score,
            "Weight": weight
        }
        self.homework_list.append(homework_data)

def save_data(environment, homework_manager):
    data = {
        "environment": {
            "setting1": environment.setting1
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

if __name__ == "__main__":
    data = load_data()

    # Initialize EnvironmentSettings and HomeworkManager objects with loaded data
    environment = EnvironmentSettings()
    environment.setting1 = data["environment"].get("setting1")

    homework_manager = HomeworkManager()
    homework_manager.homework_list = data["homework_list"]

    # Create a parser object
    parser = argparse.ArgumentParser(description="Manage environment settings and homework")

    # Define command-line flags
    parser.add_argument("--setting1", help="Set the value of setting1")
    parser.add_argument("--add-homework", action="store_true", help="Add homework")

    # Parse command-line arguments
    args = parser.parse_args()

    # Set environment settings based on command-line flags
    if args.setting1:
        environment.set_setting("setting1", args.setting1)

    if args.setting1.lower() == "weighted average":
        # Read numbers from JSON file
        with open('data.json') as json_file:
            data = json.load(json_file)
            weight1 = 40 #int(data["Weight1"])
            weight2 = 60 #int(data["Weight2"])
            score1 = 85 #int(data["Score1"])
            score2 = 90 #int(data["Score2"])

    percent = sub_weighted_avg(score1, score2, weight1, weight2)


    # Perform actions based on command-line flags
    if args.add_homework:
        # Prompt the user for homework details
        name = input("Enter the name of the homework: ")
        #substitute_method = input("Enter the substitute method (average, weighted_average, max, min, median): ")
        score = input("Enter the score of the homework: ")
        weight = input("Enter the weight of the homework: ")

        # Add the homework with the provided details
        homework_manager.add_homework(name, score, weight)

        # Save data immediately after adding a homework
        save_data(environment, homework_manager)

    # Print or manipulate the environment and homework data as needed
    print("Environment Settings:")
    print(f"Setting1: {environment.setting1}")

    print("\nHomework List:")
    for homework in homework_manager.homework_list:
        print(f"Name: {homework['Name']}")
        # print(f"ID: {homework['ID']}")
        print(f"Score: {homework['Score']}")
        print(f"Weight: {homework['Weight']}")
    print(percent)