from exit import check_if_exiting
from search import search

def get_command():
    command = input("Enter a command: ")

    check_if_exiting(command.lower())

    return command

def get_assignment(course):
    user_input = input("Enter the name of the assignment to customize (or type 'exit' to quit): ")

    check_if_exiting(user_input.lower())

    assignments = course.get_assignments()
    assignment_names = [assignment.name for assignment in assignments]
    assignment_name = search(assignment_names, user_input.lower())

    return assignment_name

def get_sub_method():
    sub_method = input("Which substitution method would you like to use? ")
    check_if_exiting(sub_method)

    valid_commands = ["substitute, exit"]
    sub_method = search(valid_commands, sub_method.lower())

    return sub_method