from input import get_assignment
from assignment_data import get_assignment_data

def avg(course, assignment_name):
    total = get_total()
    substitute_assignments = get_sub_assignments(course, total)

    assignment = get_assignment_data(course, assignment_name)
    submissions = assignment.get_submissions()

    grade_map = {}
    submission_scores = [0] * (total + 1)

    create_map(course, grade_map, submissions, submission_scores, substitute_assignments)
    
    update_grade(grade_map, total, submissions)

    #students = course.get_users()
    #for student in students:
    #    update_grade(student, course, assignment_name, substitute_assignments)

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

def update_grade(grade_map, total, submissions):
    for student in grade_map:
        sum = 0
        for i in range(1, len(grade_map[student])):
            sum+=grade_map[student][i]
        grade_map[student][0] = sum / total
    
    for submission in submissions:
        if submission.user_id in grade_map:
            submission.edit(submission={'posted_grade':grade_map[submission.user_id][0]})

def create_map(course, grade_map, submissions, submission_scores, substitute_assignments):
    for submission in submissions:
        curr_student = submission.user_id
        if submission.workflow_state=="unsubmitted" or submission.score==None:
            continue
        submission_scores[0] = submission.score
        grade_map[curr_student] = submission_scores
    
    index = 1
    for sub_assignment in substitute_assignments:
        assignment = get_assignment_data(course, sub_assignment)
        sub_submissions = assignment.get_submissions()
        for sub_submission in sub_submissions:
            if sub_submission.user_id in grade_map:
                grade_map[sub_submission.user_id][index] = sub_submission.score
        index+=1

    

