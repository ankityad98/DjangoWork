
>Steps to Run

1. Move to project root folder ($ cd logist)

2. Create and activate a virtualenv (Python 3)

>Install Dependency

3. pip install -r requirements.txt

>Make Migrations to database

4. python manage.py migrate

5. python manage.py makemigrations logistapp

6. python manage.py migrate

>Create admin user

6. Python manage.py createsuperuser

> Run development server

7. python manage.py runserver
