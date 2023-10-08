from setup import setup
from layout import command_table, sub_options
from input import get_command, get_assignment, get_sub_method
from substitutions import substitute
from object_inputs import HomeworkManager


def main():
    homework_manager = HomeworkManager()

    course = setup()
    command_table()
    command = None
    
    while command==None:
        command = get_command()               
    
        if command:
            assignment_name = None 
            while assignment_name==None:            
                assignment_name = get_assignment(course, "Enter the name of the assignment to customize (or type 'exit' to quit): ")

                if assignment_name:
                    print("Assignment found: ", assignment_name)
                    sub_options()
                    sub_method = None

                    while sub_method==None:
                        sub_method = get_sub_method()
                        if sub_method:
                            substitute(sub_method, course, homework_manager, assignment_name)
                        else:
                            print(f'Invalid substitution method.')

                else:
                    print(f'No matching assignment found.')
        else:
            print(f'No matching command found.')


if __name__ == "__main__":
    main()