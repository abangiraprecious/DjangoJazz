### venv

It is suggested to have dedicated virtual environment for each Django project. For later versions of python, we have venv (it comes with python). <br>
The name of the venv is your choice but the convention is to name is at venv for easy identification. 

**Steps**
1. Create: python3 -m venv venv
2. Activate: ource venv/bin/activate

### Install Django
Remember to install django in the venv

**Confirm you're using the venv's Python/pip**
which python3
which pip3

1. Install Django
python3 -m pip install Django==6.0.7 (or whatever version you want)

2. Confirm 
python3 -m django --version

3. Start project
python3 -m django startproject oas_bay . 
- oas_bay can be whatever project name you choose
- the . puts the manage.py file outside (in the current folder) and not in the project folder

4. Run server
python3 manage.py runserver

