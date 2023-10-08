from setup import setup
from layout import command_table, sub_options
from search import search
from input import get_command, get_assignment, get_sub_method


def main():
    course = setup()
    command_table()
    
    while True:
        command = get_command()        
        is_valid = search(command, "substitute")
    
        if is_valid:
            assignment_name = get_assignment(course)

            if assignment_name:
                sub_options()
                sub_method = get_sub_method()
                if sub_method:
                    # perform sub
                else:
                    print(f'Invalid substitution method.')

            else:
                print(f'No matching assignment found.')
        else:
            print(f'No matching command found.')


if __name__ == "__main__":
    main()