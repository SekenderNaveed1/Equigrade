from avg import get_total, get_sub_assignments, create_map
from input import get_assignment
from assignment_data import get_assignment_data

def direct(course, assignment_name):
    substitute_assignment = get_sub_assignment(course)

    assignment = get_assignment_data(course, assignment_name)
    submissions = assignment.get_submissions()

    grade_map = {}
    submission_scores = [0] * 2

    create_map(course, grade_map, submissions, submission_scores, substitute_assignment)
    
    update_grade(grade_map, submissions)

    #students = course.get_users()
    #for student in students:
    #    update_grade(student, course, assignment_name, substitute_assignments)

    return substitute_assignment

def update_grade(grade_map, submissions):
    #use the weight and the submission scores to calculate the average
    for student in grade_map:
        grade_map[student][0] = grade_map[student][1]
    
    for submission in submissions:
        if submission.user_id in grade_map:
            submission.edit(submission={'posted_grade':grade_map[submission.user_id][0]})

def get_sub_assignment(course):
    substitute_assignments = []

    assignment_name = None 
    while assignment_name==None:   
        prompt = "Enter the name of the substitution assignment: "        
        assignment_name = get_assignment(course, prompt)

        if assignment_name:
            print("Assignment found: ", assignment_name)
            substitute_assignments.append(assignment_name)
        else:
            print(f'No matching assignment found.')
    return substitute_assignments