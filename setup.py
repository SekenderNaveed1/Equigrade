import dotenv
import os
from canvasapi import Canvas

def setup():
    dotenv.load_dotenv(dotenv.find_dotenv())

    # Get the Canvas API token from the environment variables
    TOKEN = os.environ.get('CANVAS_API_TOKEN')
    BASEURL = 'https://canvas.ucdavis.edu'

    canvas_api = Canvas(BASEURL, TOKEN)

    course_id = os.getenv('course_id') #This is the course id of the Matthew Butner Sandbox it is the digits after courses, so modify as you need to access specific courses.
    
    return canvas_api.get_course(course_id)