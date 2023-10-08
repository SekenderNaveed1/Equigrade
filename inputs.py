import json

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
            print(f"\nName: {homework.name}")
            print(f"Substitute Method: {homework.substitute_method}")
            print(f"Substitute Assignments: {homework.substitute_assignments}")
            user_prompt(homework, i)

class EnvironmentSettings:
    def __init__(self, setting1=None, setting2=None):
        self.setting1 = setting1
        self.setting2 = setting2

def get_input(prompt, allowed_values):
    while True:
        user_input = input(prompt).strip()
        if user_input in allowed_values:
            return user_input

def user_prompt(homework, i):
    while True:
        answer = get_input(f"Do you want to change anything{' else' if i > 1 else ''}? (Yes/No) ", ["Yes", "No"])
        if answer == "No":
            break
        answer2 = get_input("What do you want to change? (Name/Substitute Method/Substitute Assignments) ", ["Name", "Substitute Method", "Substitute Assignments"])
        
        if answer2 == "Name":
            homework.name = input("What would you like the new name to be? ").strip()
        elif answer2 == "Substitute Method":
            homework.substitute_method = get_input("What would you like the new substitute method to be? (average/weighted_average/max/min/median) ", ["average", "weighted_average", "max", "min", "median"])
        elif answer2 == "Substitute Assignments":
            homework.substitute_assignments = input("What would you like the new substitute assignments to be? ").strip()

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
            substitute_method = get_input("Enter the substitute method (average/weighted_average/max/min/median): ", ["average", "weighted_average", "max", "min", "median"])
            substitute_assignments = input("Enter substitute assignments: ").strip()
            homework_manager.add_homework(name, substitute_method, substitute_assignments)
            save_data(environment, homework_manager)
        elif action == "show-homework":
            homework_manager.print_homework_data()
