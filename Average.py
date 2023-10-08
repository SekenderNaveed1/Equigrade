import dotenv
import os
import canvasapi
import sys
from canvasapi import Canvas
from fuzzywuzzy import fuzz, process

dotenv.load_dotenv(dotenv.find_dotenv())

# Get the Canvas API token from the environment variables
TOKEN = os.environ.get('CANVAS_API_TOKEN')
BASEURL = 'https://canvas.ucdavis.edu'

canvas_api = Canvas(BASEURL, TOKEN)



def function_to_change_grade(course, assignment_name, percentage):
    assignments = course.get_assignments()
    for assignment in assignments:
        if assignment.name == assignment_name:
            group_id = assignment.assignment_group_id
            group = course.get_assignment_group(group_id)
            group.edit(grading_standard_id=None, group_weight=percentage)  # Set the new group weight
            print(f"Group '{group.name}' weight updated to {percentage}%")
            break
    else:
        print(f"No matching assignment found with the name '{assignment_name}'.")


       



def find_assignments_weight(course, assignment_name):
   assignments = course.get_assignments()
   for assignment in assignments:
      if assignment.name == assignment_name:
         group_id = assignment.assignment_group_id
         group = course.get_assignment_group(group_id)
         return group.group_weight
   return None


def get_assignments_by_name(course, assignment_name):
  assignments = course.get_assignments()
  assignment_names = [assignment.name for assignment in assignments]
  match,score = process.extractOne(assignment_name, assignment_names, scorer=fuzz.token_set_ratio) #this is a tuple to access the match and score

  if score >= 80: # you can modify this score if you need, this is there simply to see the similiarity between the misspelling of the user and the assignment actual name
    return match
  else:
    return None
  

def get_weight_of_assignment_entered(course, assignment_name):
    assignments = course.get_assignments()
    weights = {}
    for assignment in assignments:
        assignment_info = assignment.get_assignment()
        if 'grading_weights' in assignment_info:
            weights[assignment.name] = assignment_info['grading_weights']
        return weights
    

def get_grading_scheme(course):
    return course.get_grading_standards()
   


def main():
  course_id = os.getenv('course_id') #This is the course id of the Matthew Butner Sandbox it is the digits after courses, so modify as you need to access specific courses.
  
  course = canvas_api.get_course(course_id)
  

  while True:
    user_input = input("Enter the name of the assignment (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break

        # Search for the assignment by name using FuzzyWuzzy
    assignment_name = get_assignments_by_name(course, user_input)

    if assignment_name:
        assignment_weight = find_assignments_weight(course, assignment_name)
        print(f"The weight for {assignment_name} is {assignment_weight:.2f}%.")
        user_input = input("Would you like to modify this (y/n)?: ")
        if user_input.lower() == "y":
            percent_change = input("what percent?: ")
            function_to_change_grade(course, assignment_name, percent_change)
        else:
           continue

    else:
        print(f'No matching assignment found.')

if __name__ == "__main__":
    main()