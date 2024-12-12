# Stack Used:
- Python Django
- MySQL

# Project Setup:
- open terminal and `cd` to the project folder book-library-project
- install dependencies `pip install -r requirements.txt`
- create the database `python manage.py init_db`
- create the migrations `python manage.py makemigrations`
- create the tables `python manage.py migrate`
- populate the tables `python manage.py seed_db`
- create the stored procedures `python manage.py create_procedures`
- run the server `python manage.py runserver`

# Note:
- Django models (ORM) was used for requirement 1.
- Stored Procedures were used for requirement 2.