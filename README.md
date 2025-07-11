## Creating a project

Create a folder name that folder, open the folder in vscode and run the command in terminal to create virtual environment,you can use your own name for virtual environment 'python -m venv environment_name'
```
python -m venv env
```

Run the commant to activate the environment '.\user_environment_name\Scripts\activate'
```
.\env\Scripts\activate
```

Run the command to install the requirements in the 'requirements.txt'
```
pip install -r requirements.txt
```

To create the main app, run the command 
```
django-admin startproject school_managment . 
```

For create other sub app
```
python manage.py startapp school
```

Look for 'settings.py' in main app and add 'school.apps.SchoolConfig' to the " INSTALLED_APPS " list

Look for 'models.py' in sub app and create the tables needed, run the command to create the models
```
cd school_managment

python manage.py makemigrations 

python manage.py migrate
```
