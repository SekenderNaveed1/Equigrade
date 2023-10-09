from input import get_assignment
from assignment_data import get_assignment_data

def avg(course, assignment_name):
    total = get_total()
    substitute_assignments = get_sub_assignments(course, total)

    students = course.get_users()
    for student in students:
        update_grade(student, course, assignment_name, substitute_assignments)

    return substitute_assignments

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

    for i in range(total):
        assignment_name = None 
        while assignment_name==None:   
            prompt = "Enter the name of substitution assignment " + str(i + 1) + ": "        
            assignment_name = get_assignment(course, prompt)

            if assignment_name:
                print("Assignment found: ", assignment_name)
                substitute_assignments.append(assignment_name)
            else:
                print(f'No matching assignment found.')
    
    return substitute_assignments

def update_grade(student, course, assignment_name, substitute_assignments):
    assignment = get_assignment_data(course, assignment_name)
    student_id = student.sis_user_id
    try:
        submission = assignment.get_submission(student_id)
    except:
        print("No submission found.")
        return
    
    sum = 0
    for assignment in substitute_assignments:
        assignment = get_assignment_data(course, assignment)
        try:
            sub_submission = assignment.get_submission(student_id)
        except:
            print("No substitute submission found.")
        
        if sub_submission.score is not None:
            sum+=sub_submission.score

    new_score = sum / len(substitute_assignments)

    submission.edit(submission={'posted_grade':new_score})

