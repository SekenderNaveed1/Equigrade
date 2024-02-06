Equigrade: The Ultimate Grading System

Equigrade is designed to transform educational assessment by introducing a flexible, comprehensive grading system that adapts to the nuances of student performance. Its goal is to simplify the grading process while ensuring accuracy and fairness in evaluation.

Why Equigrade?

    Save Time: Automate grading with Equigrade, allowing educators to focus on teaching and personalized feedback.
    DRY Principle: Stop reinventing the wheel for each assessment. Equigrade offers a customizable framework to meet diverse grading needs.
    Innovation in Education: Equigrade is built to address and solve the real challenges in educational assessment.

While Equigrade aims to be broadly applicable, we recognize the uniqueness of each educational context and welcome contributions to make this tool even better.
Table of Contents

    Built With
    Getting Started
        Setup
            Clone Repository
            Setting up Virtual Environment
            Installing Dependencies
            Testing Connection to CanvasAPI
    Usage
    Roadmap
    Contributing
    License
    Contact
    Acknowledgments

Built With

    Python for core functionality
    Flask for web interface (optional)
    Integration with Canvas LMS

Getting Started

Follow these steps to get a local copy up and running.
Setup
Clone Repository

    Open your terminal.
    Navigate to your directory of choice.
    Execute the command git clone https://github.com/SekenderNaveed1/Equigrade.git.
    Alternatively, you can use GitHub Desktop to clone the repository by clicking the "Code" button on the GitHub page and selecting "Open with GitHub Desktop".

Prerequisite: Ensure you have Python version 3.11 installed on your machine.
Setting up Virtual Environment

    Change directory to the cloned repository: cd Equigrade.
    Create a virtual environment by running python -m venv venv in your terminal.
    Activate the virtual environment:
        On Windows, use .\venv\Scripts\activate.
        On macOS and Linux, use source venv/bin/activate.
        You should see (venv) before your command prompt if successful.

Installing Dependencies

In your activated virtual environment:

    Run pip install -r ./requirements.txt to install the project dependencies.

Testing Connection to CanvasAPI

    Sign in to your Canvas account.
    Navigate to "Account" > "Settings".
    Scroll to "Approved Integrations" and click "New Access Token".
    Name your token, set an expiration date, and click "Generate Token".
    Copy the generated token.
    Create a .env file in the project directory and add CANVAS_API_TOKEN={Your Token Here}.
    Run python ./setup.py to test the connection. You should see your name and a number outputted in the terminal.

Usage

Equigrade is designed to enhance the grading process with features like grade substitution, integration with Canvas, and more. For detailed examples of how to use Equigrade in your projects, refer to the Documentation.
Roadmap

See the open issues for a list of proposed features (and known issues).
Contributing

Contributions are welcome! For any enhancements or bug reports, please follow the steps in the Contributing section.
License

Distributed under the MIT License. See LICENSE.txt for more information.
Contact

    Project Maintainer: [Your Name] - @your_twitter - email@example.com
    Project Link: https://github.com/your_username/Equigrade

Acknowledgments

    Choose an Open Source License
    And more listed in the Acknowledgments section.
