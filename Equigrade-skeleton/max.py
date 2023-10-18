from avg import avg
from Weightedavg import get_total, get_sub_assignments, get_assignment_data, create_map

def max_score(course, assignment_name):
    total = get_total()
    an_array_of_weights = [0] * total
    substitute_assignments = get_sub_assignments(course, total, an_array_of_weights)

    assignment = get_assignment_data(course, assignment_name)
    submissions = assignment.get_submissions()

    grade_map = {}
    submission_scores = [0] * (total + 1)

    create_map(course, grade_map, submissions, submission_scores, substitute_assignments)
    
    update_grade(grade_map, total, submissions, an_array_of_weights)

    #students = course.get_users()
    #for student in students:
    #    update_grade(student, course, assignment_name, substitute_assignments)

    return substitute_assignments

def update_grade(grade_map, total, submissions, total_weights_array):
    #use the weight and the submission scores to calculate the average
    for student in grade_map:
        wsum = 0
        sum = 0
        for i in range(1, len(grade_map[student])): #1 to end
            #print(i)
            wsum += grade_map[student][i] * total_weights_array[i-1]
            sum += grade_map[student][i]
            #print(grade_map[student][i])
        wavg = round(wsum, 2)  # Round the sum to 2 decimal places
        avg = sum / total
        grade_map[student][0] = max(wavg, avg)
    
    for submission in submissions:
        if submission.user_id in grade_map:
            submission.edit(submission={'posted_grade':grade_map[submission.user_id][0]})