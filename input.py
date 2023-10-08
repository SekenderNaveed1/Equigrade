from exit import check_if_exiting
from search import search

def get_command():
    command = input("Enter a command: ")

    check_if_exiting(command.lower())

    valid_commands = ["substitute", "exit"]    
    command = search(valid_commands, command.lower(), 80)

    return command

def get_assignment(course):
    user_input = input("Enter the name of the assignment to customize (or type 'exit' to quit): ")

    check_if_exiting(user_input.lower())

    assignments = course.get_assignments()
    assignment_names = [(assignment.name).lower() for assignment in assignments]
    assignment_name = search(assignment_names, user_input.lower(), 80)

    return assignment_name

def get_sub_method():
    sub_method = input("Which substitution method would you like to use? ")
    check_if_exiting(sub_method)

    valid_subs = ["average", "weighted average", "max"]
    sub_method = search(valid_commands, sub_method.lower(), 80)

    return sub_method