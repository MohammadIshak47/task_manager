
# Task Manager With REST API

# Overview
This project is a task management web application with a REST API built using Django. It allows multiple users to create, view, update, and delete tasks. The application utilizes Django templates for rendering views, PostgreSQL for the database, and Django ORM for managing database relations. Additionally, it incorporates virtual environments, environment variables, and Git for proper development practices.





## Technology Used
- Django==5.0.2
- djangorestframework==3.14.0
- asgiref==3.7.2
- dj-database-url==2.1.0
- dj-email-url==1.0.6
- pillow==10.2.0
- psycopg2==2.9.9
- python-dotenv==1.0.1
- pytz==2024.1
- sqlparse==0.4.4
- typing_extensions==4.9.0
- tzdata==2024.1
- django-cache-url==3.4.5
- environs==10.3.0
- marshmallow==3.20.2
- packaging==23.2








## How To Run Locally

Clone the project

```bash
  git clone https://github.com/MohammadIshak47/task_manager.git
```

Go to the project directory

```bash
  cd task_manager
```
Create a virtual environment  ( In windows)

```bash
  python -m venv myenv
```
Activate the virtual environment ( In windows)

```bash
  .\myenv\Scripts\Activate
```
Create a virtual environment  (In Linux OS)

```bash
  python3 -m venv myenv

```
Activate the virtual environment (In Linux OS)

```bash
  source myenv/bin/activate

```

Install the dependencies in requirements.txt file

```bash
  pip install -r requirements.txt
```



## Setup PostgreSQL Database

- Install PostgreSQL

```bash
  sudo apt install postgresql postgresql-contrib
``` 

- Login to PostgreSQL

```bash
  sudo -u postgres psql
``` 

- Create a database

```bash
  CREATE DATABASE newdb;
``` 

- Create a user

```bash
  CREATE USER ishak WITH PASSWORD 'Hello123';
``` 
- Grant privileges to the user

```bash
  GRANT ALL PRIVILEGES ON DATABASE newdb TO ishak;
``` 

- Exit from PostgreSQL

```bash
 \q
``` 
- Configure settings.py: Open task_manager project's settings.py file and locate the DATABASES configuration. Update it to use PostgreSQL. Replace the existing configuration with the following:

```javascript
# task_manager/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'newdb',
        'USER': ishak',
        'PASSWORD': 'Hello123',
        'HOST': '127.0.0.1',   # If PostgreSQL is running on your local machine
        'PORT': '5432',       # Default PostgreSQL port
    }
} 

```



## Setup Enviroment Variables
- Install environs[django] in task_manager directory, which allows you to use .env files to manage your environment variables.

```bash
 python -m pip install 'environs[django]'
``` 
- There are three lines of imports to add near the top of the task_manager/settings.py file.

```javascript
# task_manager/settings.py

from pathlib import Path
from environs import Env 
env = Env() 
env.read_env() 

```



- Then create a new hidden file called .env in the task_manager directory which will store our environment variables.

- The last step is to add .env to our existing .gitignore file. There’s no sense using environment variables if they will still be stored in Git! while we are updating the file we might as well as add all *.pyc files and the __pycache__- directory.

```javascript
# task_manager/.gitignore
.myenv/
.env
__pycache__/
db.sqlite3
.DS_Store # Mac only


```

- Before committing run git status to confirm all these files are being ignored as intended. Then add our new work and create a commit.

```javascript
# task_manager/shell
(.myenv) > git status
(.myenv) > git add -A
(.myenv) > git commit -m "add environment variables"

```

## DEBUG & SECRET_KEY
- If you look at the DEBUG configuration in django_project/settings.py it is currently set to True. This generates a very detailed error page and stack trace.
- For example,start up the local webserver with python manage.py runserver and visit an API endpoint that doesn’t exist such as `http://127.0.0.1:8000/api/v1/tasks/1.`

- We want DEBUG to be True for local development yet False for production. And if there is any difficulty loading the environment variables, we want DEBUG to default to False so we’re extra secure. To implement this, start by adding DEBUG=True to the .env file.





```javascript
# task_manager/.env
DEBUG=True

```

- Then in task_manager/settings.py, change the DEBUG setting to read the variable "DEBUG"
from the .env file but with a default value of False.
```javascript
# task_manager/settings.py
DEBUG = env.bool("DEBUG", default=False)

```

- If you refresh the webpage at `http://127.0.0.1:8000/api/v1/tasks/1.`, you’ll see the full local error page is still there. Everything is working properly.

- The next setting to change is SECRET_KEY which is a random 50 character string generated each time startproject is run. If you look at the current value in task_manager/settings.py it starts with django-insecure to indicate the current value is not secure.

- The solution is to generate a new secret key and to store that value in an environment variable so
it never touches source control. One way to generate a new one is by invoking Python’s built-in secrets115 module by running python -c 'import secrets; print(secrets.token_urlsafe())' on the command line.

```bash
 python -c "import secrets; print(secrets.token_urlsafe())"
KBl3sX5kLrd2zxj-pAichjT0EZJKMS0cXzhWI7Cydqc
``` 

- Copy and paste this new value into the .env file under the variable SECRET_KEY.

```javascript
# task_manager/.env
DEBUG=True
SECRET_KEY=KBl3sX5kLrd2zxj-pAichjT0EZJKMS0cXzhWI7Cydqc

```

- Finally, switch over SECRET_KEY in the task_manager/settings.py file to read from the
environment variable now.

```javascript
# task_manager/settings.py
SECRET_KEY = env.str("SECRET_KEY")

```


- Make Changes to Models: First, make the necessary changes to your Django models in your models.py file


```bash
 python manage.py makemigrations

```
- Apply Migrations: To apply the migrations and update your database schema, run the following command:

```bash
 python manage.py migrate

```
- To confirm everything is working properly restart the local server with python manage.py
runserver and refresh any API endpoint on our site. It should be working normally.

```bash
 python manage.py runserver

```
- Open the browser and go to http://127.0.0.1:8000/

- To login admin panel create superuser 

```bash
  python manage.py createsuperuser
```

- After creating superuser successfully  Open the browser and go to http://127.0.0.1:8000/

- To access the admin panel, go to http://127.0.0.1:8000/admin/

- Login with the following credentials:

- Username: admin
- Password: admin

- Now you can access the admin panel with the credentials you have just created





To deactivate the virtual environment
```bash
  deactivate
```

## Task Manager Apps Features/Functionalities:

- User Authentication (Registration, Login,Logout).

- Task properties include title, description, due date, multiple photos add/delete options, priority (low, medium, high), option to mark as complete, creation date, and optional last update date.
- Task searching and filtering by title, creation date, due date, priority, and completion status.
- Task details page displaying all information including photos.
- Update task functionality with all fields.
- Task deletion with confirmation.

## Task Manager Apps  API Endpoints Access 

- To see All task list : Endpoint
```bash
   http://127.0.0.1:8000/api/v1/tasks/
```

- To see  single task

 ```bash
   http://127.0.0.1:8000/api/v1/tasks/5
```

- To See Task Details & Update an Existing Task: Endpoint
```bash
   http://127.0.0.1:8000/api/v1/tasks/5
```

- To create any task 
```bash
   http://127.0.0.1:8000/api/v1/tasks/
```

- To Delete Task Call this endpoint to update a task with a specific id

```bash
   http://127.0.0.1:8000/api/v1/tasks/5
```


















