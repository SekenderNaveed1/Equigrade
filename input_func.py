

def get_int(prompt, max_len = 30):
    number = input(prompt).strip()
    while True:
        if number.isnumeric() and int(number) <= int(max_len):
            return number
        elif int(number) > int(max_len):
            number = input(f"Please enter an integer less than {int(max_len)+1}: ")
        else:
            number = input("Please enter a valid integer: ")
def get_substitute_assignments(number_of_substitute_assignments):
    substitute_assignments = []
    for i in range(int(number_of_substitute_assignments)):
        substitute_assignments.append(input(f"Enter the name of substitute assignment {i+1}: ").strip())
    return substitute_assignments

def get_input(prompt, allowed_values):
    while True:
        user_input = input(prompt).strip()
        if user_input in allowed_values:
            return user_input

def validate_homework(homework):
        answer2 = get_input("What do you want to change? (Name/Substitute Method/Substitute Assignments) ", ["Name", "Substitute Method", "Substitute Assignments"])
        
        if answer2 == "Name":
            homework.name = input("What would you like the new name to be? ").strip()
        elif answer2 == "Substitute Method":
            homework.substitute_method = get_input("What would you like the new substitute method to be? (average/weighted_average/max/min/median) ", ["average", "weighted_average", "max", "min", "median"])
        elif answer2 == "Substitute Assignments":
            number_of_sub_assignments = get_int("How many substitute assignments would you like?: ")
            homework.substitute_assignments = get_substitute_assignments(number_of_sub_assignments)
