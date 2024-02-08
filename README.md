Equigrade: A more hoslitic Grading System
![alt text](https://github.com/SekenderNaveed1/Equigrade/blob/main/Logo.png)
Equigrade is designed to transform educational assessment by introducing a flexible, comprehensive grading system that adapts to the nuances of student performance. Its goal is to simplify the grading process while ensuring accuracy and fairness in evaluation.

What is Equigrade?
Equigrade is an innovative grading system designed to enhance the way educators assess student performance. At its core, Equigrade provides flexibility and accuracy in grading, allowing for the substitution and adjustment of grades based on predefined rules or instructor discretion. This system is built to reflect a student's true capabilities by considering their overall performance rather than just isolated outcomes.

Equigrade's key features include:

    Grade Substitution: If a student performs poorly on one assignment but improves on a similar one later, Equigrade can substitute the latter grade for the former, ensuring the grading reflects the student's learning curve.
    Holistic Assessment: By taking into account the entirety of a student's work, Equigrade promotes a more comprehensive view of their knowledge and skills.
    Customizable Settings: Instructors can adjust the system to fit their specific grading criteria, making Equigrade versatile across different subjects and teaching methods.
    Integration with Canvas: Designed to work seamlessly with the Canvas Learning Management System (LMS), Equigrade ensures a smooth user experience for both instructors and students.

While Equigrade aims to be broadly applicable, we recognize the uniqueness of each educational context and welcome contributions to make this tool even better.
Table of Contents

Built With

    Python for core functionality
    Integration with Canvas LMS

# Clone Repository

- In your directory of choice enter 
``` git clone https://github.com/SekenderNaveed1/Equigrade.git ``` into the terminal
- or you can click ``` code ``` and ``` clone with github desktop ``` in github
![image](https://github.com/SekenderNaveed1/Equigrade/assets/99291169/f9493a75-7701-41d9-8097-cc2ce04c6a93)

Make sure you have python version 3.11 installed

# Setting up virtual environment

1. cd into the directory with the code
- In your terminal, enter ``` python -m venv venv ```.  The ``` venv ``` folder should be in the same directory as ``` main.py ```
- To activate your virtual environment, enter ``` ./venv/Scripts/activate ``` into the terminal.  There should be a ``` (venv) ``` to the left of your prompt now.
- To deactivate your virtual environment, enter ``` deactivate ```

# Installing dependencies

- In your virtual environment, enter ``` pip install -r ./requirements.txt ``` in the terminal.  

## Testing Connection to canvasAPI
1. Go to your canvas page and sign in
2. Click on ``` Account ```, then ``` Settings ```.
3. Scroll down until you see ``` Approved Integrations: ```.
4. Click ``` New Access Token ```.  Name the access token and give it an expiration date, then click generate token.
5. Copy the access token to your clipboard.
6. Go back to your IDE and create a file named ``` .env ``` in the same directory as ``` setup.py ```.
7. In the .env file, type ``` CANVAS_API_TOKEN = {Paste your access token here} ```.
8. Run setup.py: ``` python ./setup.py ```.
9. The terminal should have outputed your name with a number.


Usage

Equigrade is designed to enhance the grading process with features like grade substitution, integration with Canvas, and more. For detailed examples of how to use Equigrade in your projects, refer to the Documentation.


Roadmap

See the open issues for a list of proposed features (and known issues).
Contributing

Contributions are welcome! For any enhancements or bug reports, please follow the steps in the Contributing section.
- Please email me at sekendernaveed1@gmail.com with the proposed changes. I will take a look and get back to you asap.

License ```LGPL-2.1 license```

Distributed under the MIT License. See LICENSE.txt for more information.
Contact

    Project Maintainer/Manager: Naveed Sekender - sekendernaveed1@gmail.com
    Project Link: (https://github.com/SekenderNaveed1/Equigrade)

Acknowledgments

    Special thanks to:
    Matthew Butner - UC Davis Faculty Member
    Gavin Lang  - Lead of QA team
    Amabel Gale - Lead of DEV team
