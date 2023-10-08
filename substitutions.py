from avg import avg
from sub_weighted_avg import weighted_avg

def substitute(sub_method, course, homework_manager, assignment_name):
    if sub_method == "average":
        new_score, sub_assignments = avg(course)

    elif sub_method == "weighted_average":
        new_score, sub_assignments = weighted_avg(course)
        
    else:
        avg_score, sub_assignments_avg = avg(course)
        weighted_avg_score, sub_assignments_weighted_avg = weighted_avg(course)

        new_score = max(avg_score, weighted_avg_score)

        if (new_score == avg_score): # Need to change this to account for possibility of avg_score and weighted_avg_score being the same
            sub_assignments = sub_assignments_avg
        else:
            sub_assignments = sub_assignments_weighted_avg
    
    substitute_assignments = sub_assignments
    homework_manager.add_homework(assignment_name, sub_method, substitute_assignments)
    
    return new_score

