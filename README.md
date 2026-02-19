# Task Management REST API

A RESTful API built with Django and Django REST Framework (DRF) that enables users to manage tasks efficiently.

The API provides secure authentication, full CRUD functionality, and task status tracking, making it ideal for web and mobile task management applications.

---

## Features

- User Authentication (Register, Login, Logout)
- Create, Read, Update, Delete (CRUD) tasks
- Task status tracking (Pending / Completed)
- Due dates and priority levels
- Filtering and searching tasks
- User-based data isolation
- RESTful JSON responses

---

## Tech Stack

- Backend: Django
- API Framework: Django REST Framework
- Database: SQLite (default, can be changed to PostgreSQL/MySQL)
- Authentication: Token or JWT

---

## Project Structure

task_manager_api/
│
├── manage.py
├── requirements.txt
│
├── config/
│ ├── settings.py
│ ├── urls.py
│ └── asgi.py / wsgi.py
│
├── tasks/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── permissions.py
│
└── users/ (optional)


---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api

2. Create a virtual environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py migrate

5. Create superuser (optional)
python manage.py createsuperuser

6. Run the server
python manage.py runserver


API base URL:

http://127.0.0.1:8000/api/

Authentication

Example header (Token):

Authorization: Token your_token_here

API Endpoints
Authentication
Method	Endpoint	Description
POST	/api/auth/register/	Register user
POST	/api/auth/login/	Login user
POST	/api/auth/logout/	Logout user
Tasks
Method	Endpoint	Description
GET	/api/tasks/	List tasks
POST	/api/tasks/	Create task
GET	/api/tasks/{id}/	Retrieve task
PUT/PATCH	/api/tasks/{id}/	Update task
DELETE	/api/tasks/{id}/	Delete task
Task Object Example
{
  "id": 1,
  "title": "Finish project report",
  "description": "Complete and submit the final report",
  "status": "Pending",
  "priority": "High",
  "due_date": "2026-03-01",
  "created_at": "2026-02-18T10:00:00Z"
}

Running Tests
python manage.py test

Use Cases

Personal productivity apps

Team task management systems

Mobile to-do list apps

Learning project for Django REST Framework

Future Improvements

File attachments

Notifications and reminders

Team collaboration

Analytics dashboard

Docker support

Contributing

Fork the repository

Create a feature branch

Commit changes

Open a Pull Request
