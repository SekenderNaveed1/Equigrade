import dotenv
import os
import canvasapi
import sys  # Import the sys module

dotenv.load_dotenv(dotenv.find_dotenv())

TOKEN = os.environ.get('CANVAS_API_TOKEN')
BASEURL = 'https://canvas.ucdavis.edu'

canvas_api = canvasapi.Canvas(BASEURL, TOKEN)

result = canvas_api.get_user('self')


print("Python version:", sys.version)
print(result)