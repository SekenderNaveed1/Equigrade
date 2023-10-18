def get_assignment_data(course, assignment_name):
    assignments = course.get_assignments()
    for assignment in assignments:
        if assignment.name.lower() == assignment_name:
            return assignment
    return None
