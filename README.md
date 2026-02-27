# 🚀 Task Management API
Production-Grade Django REST Backend

A scalable, secure, and cloud-ready Task Management API built with Django and Django REST Framework.
This project showcases production-level backend architecture, relational database modeling, secure authentication, environment-driven configuration, and deployment practices suitable for real-world SaaS applications.

---

## 🧠 Executive Summary

The API enables authenticated users to manage categorized tasks with enterprise-ready capabilities:

- JWT-based authentication
- Extended user profiles
- Task categorization
- Filtering & pagination
- Email integration
- PostgreSQL production setup
- Cloud deployment readiness

The system is structured with clean separation of concerns and scalable backend engineering principles.

---

## 🏗 System Architecture

taskmanager/
│
├── taskmanager/              # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/                    # Core domain logic
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── signals.py
│
├── manage.py
├── requirements.txt
├── Procfile
└── runtime.txt

Architectural Principles

- RESTful resource design
- Stateless JWT authentication
- Environment-based configuration
- User-scoped querysets for data isolation
- Modular Django app structure
- Production-first mindset

---

## ✨ Core Features

### 🔐 Authentication & Authorization
- JWT authentication (SimpleJWT)
- Access & refresh tokens
- Protected endpoints
- User-specific data isolation

### 👤 User Profile System
- One-to-one extension of Django User model
- Automatic profile creation via signals
- Extensible architecture

### 📋 Task Management
- Create, retrieve, update, and delete tasks
- Due dates and priority levels
- Completion tracking
- Ownership enforcement

### 🗂 Task Categorization
- Assign tasks to categories
- Filter tasks by category
- Enforced foreign key relationships

### 📊 Filtering & Pagination
- PageNumberPagination
- django-filter integration
- Controlled query exposure

### 📧 Email Integration
- Console backend for development
- SMTP-ready for production
- Extensible reminder support

### 📘 API Documentation
- OpenAPI 3 schema
- Swagger UI
- Auto-generated via drf-spectacular

---

## 🗄 Database Design (ER Overview)

User (1) ─── (1) Profile  
User (1) ─── (M) Task  
Category (1) ─── (M) Task  

Design Rationale

- Profiles separated to preserve authentication integrity
- Tasks scoped per user for strict data isolation
- Categories normalized to prevent redundancy
- Foreign keys enforce referential integrity
- Timestamps support auditing and tracking

---

## 🛠 Technology Stack

Language: Python 3.12  
Framework: Django  
API: Django REST Framework  
Auth: SimpleJWT  
Dev Database: SQLite  
Prod Database: PostgreSQL  
Server: Gunicorn  
Static Files: WhiteNoise  
Filtering: django-filter  
Docs: drf-spectacular  
Deployment: Render / Heroku  

---

## ⚙️ Local Development Setup

### Clone Repository
git clone https://github.com/yourusername/task-management-api.git
cd task-management-api

### Create Virtual Environment

Windows
python -m venv venv
venv\Scripts\activate

Mac / Linux
python3 -m venv venv
source venv/bin/activate

### Install Dependencies
pip install -r requirements.txt

### Apply Migrations
python manage.py makemigrations
python manage.py migrate

### Create Superuser
python manage.py createsuperuser

### Run Development Server
python manage.py runserver

Swagger Docs
http://127.0.0.1:8000/api/docs/

---

## 🔐 Authentication Flow

Register
POST /api/register/

Obtain Token
POST /api/token/

Response
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}

Authenticated Requests
Authorization: Bearer <access_token>

Refresh Token
POST /api/token/refresh/

---

## 📡 API Endpoint Overview

Tasks
GET     /api/tasks/
POST    /api/tasks/
GET     /api/tasks/{id}/
PUT     /api/tasks/{id}/
DELETE  /api/tasks/{id}/

Categories
GET     /api/categories/
POST    /api/categories/

Profile
GET     /api/profile/
PUT     /api/profile/

---

## 🗄 Database Strategy

Development
- SQLite for simplicity

Production
- PostgreSQL
- Environment variable configuration
- dj-database-url integration
- Connection pooling enabled

---

## 🚀 Deployment Strategy

Render (Recommended)
1. Push project to GitHub
2. Create a Web Service on Render
3. Configure environment variables
4. Deploy and run migrations

Heroku
heroku login
heroku create your-app-name
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set SECRET_KEY=your-secret
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=your-app.herokuapp.com
git push heroku main
heroku run python manage.py migrate

---

## 🔒 Security Considerations

- DEBUG disabled in production
- Secrets stored in environment variables
- Stateless JWT authentication
- Secure cookies enabled
- SSL redirect enforced
- XSS and content-type protections
- User-scoped querysets
- Referential integrity enforced

---

## 📈 Scalability & Extensibility

- Celery + Redis for background jobs
- Scheduled email reminders
- Role-Based Access Control (RBAC)
- Real-time updates (WebSockets)
- Docker containerization
- CI/CD pipeline integration
- Horizontal scaling
- Monitoring & observability

---

## 👨‍💻 Author

Eyob Abera
