def get_score(assignment_name, course):
    students = course.get_users()

    for student in students:
        print(student)