from exit import check_if_exiting
from search import search
from parse_hw_name import split_name_num

def get_command():
    command = input("Enter a command: ")

    check_if_exiting(command.lower())

    valid_commands = ["substitute", "exit"]    
    command = search(valid_commands, command.lower(), 80)

    return command

def get_assignment(course):
    user_input = input("Enter the name of the assignment to customize (or type 'exit' to quit): ")

    check_if_exiting(user_input.lower())

    # Separate assignment name and number to allow misspellings in name but no error in number
    input_name, input_num = split_name_num(user_input)

    assignments = course.get_assignments()
    assignment_names = [(assignment.name).lower() for assignment in assignments]

    # Separate existing assignment names into name and number to compar to input name and number
    target_names = []
    target_nums = []
    for name in assignment_names:
        target_name, target_num = split_name_num(name)
        target_names.append(target_name)
        target_nums.append(target_num)

    valid_name = search(target_names, input_name, 80)
    if (input_num != []):
        valid_num = search(target_nums, input_num, 100)
    
    if (input_name and not valid_name) or (input_num and not valid_num):
        return None

    assignment_name = valid_name + valid_num

    return assignment_name

def get_sub_method():
    sub_method = input("Which substitution method would you like to use? ")
    check_if_exiting(sub_method)

    valid_subs = ["average", "weighted average", "max"]
    sub_method = search(valid_subs, sub_method.lower(), 80)

    return sub_method