from avg import avg
from Weightedavg import weighted_avg

def substitute(sub_method, course, homework_manager, assignment_name):
    if sub_method == "average":
        sub_assignments = avg(course, assignment_name)

    elif sub_method == "waverage":
        sub_assignments = weighted_avg(course, assignment_name)

    else:
        max()
    
    substitute_assignments = sub_assignments
    homework_manager.add_homework(assignment_name, sub_method, substitute_assignments)

    print("The assignment has been updated.")