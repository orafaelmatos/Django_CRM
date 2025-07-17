# Django CRM System

A lightweight **Customer Relationship Management (CRM)** application built with Django. This project demonstrates essential features for managing client data in a real-world business context, including user authentication, CRUD operations, and a clean, responsive interface.

---

## 🌐 Live Demo
Access the application here:  
<a href="https://django-crm-f9tm.onrender.com" target="_blank" style="text-decoration:none; pointer-events:auto; user-select:none;">
    <strong>👉 https://django-crm.onrender.com</strong>
</a>
---

## 📌 Project Objective
The purpose of this project is to create a simple yet practical CRM system for educational and testing purposes, providing functionality for user management and client tracking.

---

## ✅ Features
- **Secure Authentication**
  - User login and logout
  - User registration
- **Client Management**
  - Create, edit, and delete client records
  - View client data in a responsive table
- **Additional Features**
  - Form validation and error handling
  - Django Admin panel for advanced management

---

## 🛠️ Technologies Used
- **Backend:** Django (Python 3.x)
- **Database:** SQLite (default) – easy to switch to PostgreSQL or MySQL
- **Frontend:** HTML, CSS, Bootstrap for responsive UI

---

# Run locally (Optional)
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

# Notes
This project uses SQLite, which is built-in and ideal for local or academic use.

You can easily switch to PostgreSQL or MySQL in settings.py for production.

# License
This project is free to use for educational and testing purposes.
