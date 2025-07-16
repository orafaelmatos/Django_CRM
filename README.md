# Django CRM System
A basic Customer Relationship Management (CRM) project built with Django and SQLite for educational and practical learning purposes.

## Project Objective
The main goal of this project is to build a lightweight system for managing clients, simulating real-world scenarios where businesses need to keep track of customer information.

## The system allows users to:
  - Log in and log out securely
  - Register new users
  -  Create, edit, and delete client records
  -  Display client data in a clean table view

## Technologies Used
  - Python 3.x
  - Django (Web Framework)
  - SQLite (default database)
  - Bootstrap (for responsive UI)

## Features
  - User authentication (login/logout)
  - User registration
  - CRUD operations for client data
  - Client list displayed in table format
  - Form validation and error handling

# Getting Started
1. Clone the Repository
```
bash
Copy
Edit
git clone https://github.com/your-username/Django_CRM.git
cd Django_CRM
```
3. Create and activate a virtual environment
```
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
5. Install dependencies
```
bash
Copy
Edit
pip install -r requirements.txt
```
6. Apply migrations and run the server
```
bash
Copy
Edit
python manage.py migrate
python manage.py runserver
```
Now visit: http://localhost:8000

## Default Credentials (for demo/testing)
You can create a default superuser to access Django Admin:
```
bash
Copy
Edit
python manage.py createsuperuser
```
# Notes
This project uses SQLite, which is built-in and ideal for local or academic use.

You can easily switch to PostgreSQL or MySQL in settings.py for production.

# License
This project is free to use for educational and testing purposes.
