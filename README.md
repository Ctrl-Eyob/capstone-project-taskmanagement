📌 Task Management API

A RESTful API built with Django and Django REST Framework that allows users to manage tasks efficiently.
The API supports authentication, full CRUD operations, and task status tracking, making it ideal for web or mobile task management applications.

🚀 Project Overview

The Task Management API enables users to:

Register and authenticate securely

Create, update, and delete tasks

Mark tasks as complete or incomplete

Retrieve only their own tasks

Filter and paginate results

This project demonstrates best practices in REST API design, authentication, and scalable Django architecture.

🧱 Tech Stack

Backend: Django

API Framework: Django REST Framework

Database: SQLite (development) / PostgreSQL (production)

Authentication: JWT (SimpleJWT)

Deployment: PythonAnywhere or Heroku

📂 Project Structure
task_manager_api/
│
├── config/                # Project settings & URLs
├── apps/
│   ├── users/             # User management
│   └── tasks/             # Task functionality
│
├── requirements.txt
├── manage.py
└── README.md

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/yourusername/task-manager-api.git
cd task-manager-api

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py migrate

5️⃣ Create Superuser
python manage.py createsuperuser

6️⃣ Start Development Server
python manage.py runserver


API will be available at:

http://127.0.0.1:8000/api/v1/

🔐 Authentication

This API uses JWT Authentication.

Obtain Token
POST /api/v1/auth/login/


Response:

{
  "access": "your-access-token",
  "refresh": "your-refresh-token"
}


Use token in headers:

Authorization: Bearer <access_token>

📡 API Endpoints
Auth
Method	Endpoint	Description
POST	/auth/register/	Register
POST	/auth/login/	Login
POST	/auth/refresh/	Refresh token
Users
Method	Endpoint	Description
GET	/users/me/	Current user
Tasks
Method	Endpoint	Description
GET	/tasks/	List tasks
POST	/tasks/	Create task
GET	/tasks/{id}/	Retrieve task
PATCH	/tasks/{id}/	Update task
DELETE	/tasks/{id}/	Delete task
PATCH	/tasks/{id}/complete/	Toggle status
🧩 Task Model
Field	Type	Description
id	Integer	Primary key
title	String	Task title
description	Text	Details
status	Boolean	Complete or not
due_date	Date	Optional
created_at	DateTime	Auto timestamp
updated_at	DateTime	Auto timestamp
🧪 Running Tests
python manage.py test

🌍 Deployment
PythonAnywhere

Create a virtualenv

Install requirements

Configure environment variables

Run migrations

Reload web app

Heroku (Optional)
heroku create
git push heroku main
heroku run python manage.py migrate

🔒 Security Features

JWT authentication

User-specific querysets

Environment variables for secrets

Permission classes

CSRF protection (session endpoints)

📈 Future Improvements

Task categories

Notifications / reminders

File attachments

API documentation (Swagger)

Async background jobs (Celery)

🤝 Contributing

Fork the repo

Create feature branch

git checkout -b feature-name


Commit changes

git commit -m "Add feature"


Push and open Pull Request

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Eyob Abera
Backend Developer | Django & DRF
