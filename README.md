# Part 2 - Setting up Python and Django
## Install Python3, pip and venv
```
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.11
sudo apt install -y build-essential libssl-dev python3-dev
sudo apt install python3-pip python3-venv -y
```
## Create a virtual environment
```
mkdir project-envs
cd project-envs
python3 -m venv django_venv
```
## Activate the virtual environment
```
source ~/Documents/project-envs/django_venv/bin/activate
```
## Upgrade pip and install Django 3.2
```
pip install -U pip wheel setuptools
pip install django==3.2
```
## Start a Django project
```
mkdir netauto-django
cd netauto-django
django-admin startproject simplenetauto .
python manage.py startapp webconfigapp
```
## Add app to the project
* Open settings.py and add webconfigapp in the INSTALLED_APPS
## Run the development server
```
python manage.py runserver
```
* Open your browser and visit http://127.0.0.1:8000
## Update requrements.txt file
```
pip freeze > requirements.txt
```
* Some like using the above method, I like to add the name of the package installed to keep the file small and clean.