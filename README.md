# capstone-project-taskmanagement
🚀 Project Overview
A robust RESTful API for managing tasks with user authentication, allowing users to perform CRUD operations on tasks, organize them with categories and tags, and track completion status. Built with Django REST Framework.

📑 Table of Contents
Features

Tech Stack

Database Schema

API Endpoints

Installation

Configuration

Usage

Testing

Deployment

API Documentation

Contributing

License

✨ Features
Core Features
User authentication and authorization (JWT)

Complete CRUD operations for tasks

Mark tasks as complete/incomplete

Task categorization

Task tagging system

Subtask management

File attachments

Due date reminders

Task history/audit trail

Search and filtering

Advanced Features
Task prioritization (Low, Medium, High, Critical)

Task status tracking (Pending, In Progress, Completed, Cancelled)

Due date management

Task comments and collaboration

Activity logging

Pagination support

Rate limiting

🛠️ Tech Stack
Backend
Python 3.10+

Django 4.2+

Django REST Framework 3.14+

PostgreSQL (Production)

SQLite (Development)

Authentication
JWT (django-rest-framework-simplejwt)

Additional Tools
drf-spectacular (API documentation)

django-cors-headers (CORS support)

django-filter (Filtering)

celery (Async tasks for reminders)

redis (Message broker)

gunicorn (WSGI server)

📊 Database Schema
Entity Relationship Diagram
https://path-to-your-erd-image.png

Tables Overview
Users Table
Field	Type	Constraints	Description
id	integer	PK, Auto-increment	User ID
username	varchar(150)	Unique, Not null	Username
email	varchar(254)	Unique, Not null	Email address
password_hash	varchar(128)	Not null	Hashed password
first_name	varchar(150)		First name
last_name	varchar(150)		Last name
is_active	boolean	Default: true	Account status
date_joined	timestamp	Auto	Registration date
Tasks Table
Field	Type	Constraints	Description
id	integer	PK, Auto-increment	Task ID
user_id	integer	FK, Not null	Owner ID
category_id	integer	FK	Category ID
title	varchar(200)	Not null	Task title
description	text		Task description
status	varchar(20)	Not null	pending/in_progress/completed
priority	varchar(20)	Not null	low/medium/high/critical
due_date	date		Due date
created_at	timestamp	Auto	Creation time
completed_at	timestamp		Completion time
Categories Table
Field	Type	Constraints	Description
id	integer	PK, Auto-increment	Category ID
user_id	integer	FK, Not null	Owner ID
name	varchar(100)	Not null	Category name
color_code	varchar(7)	Default: '#4A90E2'	Color hex code
Tags Table
Field	Type	Constraints	Description
id	integer	PK, Auto-increment	Tag ID
user_id	integer	FK, Not null	Owner ID
name	varchar(50)	Not null	Tag name
color_code	varchar(7)	Default: '#808080'	Color hex code
🔌 API Endpoints
Authentication Endpoints
Method	Endpoint	Description	Auth
POST	/api/auth/register/	Register new user	No
POST	/api/auth/login/	Login user	No
POST	/api/auth/token/refresh/	Refresh token	No
POST	/api/auth/logout/	Logout user	Yes
POST	/api/auth/password/change/	Change password	Yes
POST	/api/auth/password/reset/	Request password reset	No
User Endpoints
Method	Endpoint	Description	Auth
GET	/api/users/profile/	Get user profile	Yes
PUT	/api/users/profile/	Update profile	Yes
PATCH	/api/users/profile/	Partial update	Yes
Task Endpoints
Method	Endpoint	Description	Auth
GET	/api/tasks/	List all tasks	Yes
POST	/api/tasks/	Create task	Yes
GET	/api/tasks/{id}/	Get task details	Yes
PUT	/api/tasks/{id}/	Update task	Yes
PATCH	/api/tasks/{id}/	Partial update	Yes
DELETE	/api/tasks/{id}/	Delete task	Yes
POST	/api/tasks/{id}/complete/	Mark complete	Yes
POST	/api/tasks/{id}/incomplete/	Mark incomplete	Yes
GET	/api/tasks/completed/	List completed tasks	Yes
GET	/api/tasks/pending/	List pending tasks	Yes
GET	/api/tasks/overdue/	List overdue tasks	Yes
Category Endpoints
Method	Endpoint	Description	Auth
GET	/api/categories/	List categories	Yes
POST	/api/categories/	Create category	Yes
GET	/api/categories/{id}/	Get category	Yes
PUT	/api/categories/{id}/	Update category	Yes
DELETE	/api/categories/{id}/	Delete category	Yes
GET	/api/categories/{id}/tasks/	Tasks in category	Yes
Tag Endpoints
Method	Endpoint	Description	Auth
GET	/api/tags/	List tags	Yes
POST	/api/tags/	Create tag	Yes
GET	/api/tags/{id}/	Get tag	Yes
PUT	/api/tags/{id}/	Update tag	Yes
DELETE	/api/tags/{id}/	Delete tag	Yes
GET	/api/tags/{id}/tasks/	Tasks with tag	Yes
Subtask Endpoints
Method	Endpoint	Description	Auth
GET	/api/tasks/{task_id}/subtasks/	List subtasks	Yes
POST	/api/tasks/{task_id}/subtasks/	Create subtask	Yes
PUT	/api/subtasks/{id}/	Update subtask	Yes
DELETE	/api/subtasks/{id}/	Delete subtask	Yes
POST	/api/subtasks/{id}/toggle/	Toggle completion	Yes
Comment Endpoints
Method	Endpoint	Description	Auth
GET	/api/tasks/{task_id}/comments/	List comments	Yes
POST	/api/tasks/{task_id}/comments/	Add comment	Yes
DELETE	/api/comments/{id}/	Delete comment	Yes
Attachment Endpoints
Method	Endpoint	Description	Auth
GET	/api/tasks/{task_id}/attachments/	List attachments	Yes
POST	/api/tasks/{task_id}/attachments/	Upload file	Yes
DELETE	/api/attachments/{id}/	Delete attachment	Yes
Query Parameters
text
?status=pending           Filter by status
?priority=high           Filter by priority
?category_id=1           Filter by category
?tag_id=1,2,3            Filter by tags
?due_date_after=2024-01-01  Due date range
?due_date_before=2024-12-31
?search=keyword          Search in title/description
?ordering=-due_date      Sort by field
?page=1                  Pagination
?page_size=20            Items per page
💻 Installation
Prerequisites
Python 3.10+

pip

virtualenv

PostgreSQL (optional, for production)

Local Setup
Clone the repository

bash
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api
Create virtual environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Set up environment variables

bash
cp .env.example .env
# Edit .env with your configuration
Run migrations

bash
python manage.py migrate
Create superuser

bash
python manage.py createsuperuser
Run development server

bash
python manage.py runserver
⚙️ Configuration
Environment Variables
env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:password@localhost:5432/taskdb
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-password
REDIS_URL=redis://localhost:6379
Settings Structure
text
settings/
├── base.py      # Common settings
├── dev.py       # Development settings
└── prod.py      # Production settings
📖 Usage
Example API Calls
Register User

bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "secure123",
    "first_name": "John",
    "last_name": "Doe"
  }'
Login

bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "secure123"
  }'
Create Task

bash
curl -X POST http://localhost:8000/api/tasks/ \
  -H "Authorization: Bearer <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project",
    "description": "Finish API documentation",
    "priority": "high",
    "due_date": "2024-12-31",
    "category_id": 1
  }'
Mark Task Complete

bash
curl -X POST http://localhost:8000/api/tasks/1/complete/ \
  -H "Authorization: Bearer <your-token>"
🧪 Testing
Run Tests
bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.tasks

# Run with coverage
coverage run manage.py test
coverage report
coverage html
Test Coverage Goals
Models: 100%

Views: 90%

Serializers: 95%

Utilities: 85%
