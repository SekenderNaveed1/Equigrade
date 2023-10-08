from input import get_assignment
from get_student_grades import get_score


def avg(course):
    total = get_total()
    substitute_assignments = get_sub_assignments(course, total)

    new_score = ""
    return new_score, substitute_assignments

def get_total():
    total = None
    while total==None:
        user_input = input("How many assignments do you want to take the average of? ")

        try:
            value = int(user_input)
            total = value
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    return total

def get_sub_assignments(course, total):
    substitute_assignments = []
    scores = []

    for i in range(total - 1):
        assignment_name = None 
        while assignment_name==None:   
            prompt = "Enter the name of substitution assignment " + str(i + 1) + ": "        
            assignment_name = get_assignment(course, prompt)

            if assignment_name:
                print("Assignment found: ", assignment_name)
                substitute_assignments.append(assignment_name)

                get_score(assignment_name, course)
            else:
                print(f'No matching assignment found.')
    
    return substitute_assignments
