from setup import setup
from layout import command_table, sub_options
from search import search
from input import get_command, get_assignment, get_sub_method
from substitutions import substitute


def main():
    course = setup()
    command_table()
    command = None
    
    while command==None:
        command = get_command()               
    
        if command:
            assignment_name = None 
            while assignment_name==None:            
                assignment_name = get_assignment(course)

                if assignment_name:
                    print("Assignment found: ", assignment_name)
                    sub_options()
                    sub_method = get_sub_method()
                    if sub_method:
                        substitute(sub_method)
                    else:
                        print(f'Invalid substitution method.')

                else:
                    print(f'No matching assignment found.')
        else:
            print(f'No matching command found.')


if __name__ == "__main__":
    main()