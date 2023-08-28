# Table of Contents

- Setup
  - [Clone repository](#clone-repository)
  - [Setting up virtual evironment](#setting-up-virtual-environment)
  - [Installing dependencies](#installing-dependencies)
  - [Testing canvasAPI](#testing-connection-to-canvasapi)

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
