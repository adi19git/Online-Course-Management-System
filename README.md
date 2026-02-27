# 📚 OCMS — Online Course Management System

A full-stack web application built using **Django + Django REST Framework + JavaScript** that allows students to browse courses, enroll in them, and allows admins to monitor platform analytics.

---

## 🚀 Features

### 👨‍🎓 Student

* User login using JWT authentication
* View all available courses
* Enroll in a course
* Persistent login (token stored in browser)

### 👨‍💼 Admin

* View total users
* View total courses
* View total enrollments
* Analytics dashboard

### ⚙️ System

* REST API backend
* Template-based frontend
* Course caching (Redis/Local cache)
* Secure token authentication

---

## 🏗️ Tech Stack

| Layer          | Technology             |
| -------------- | ---------------------- |
| Backend        | Django                 |
| API            | Django REST Framework  |
| Authentication | JWT (SimpleJWT)        |
| Frontend       | HTML, CSS, JavaScript  |
| Database       | Postgresql             |
| Caching        | Django Cache Framework |

---

## 📂 Project Structure

```
Online-Course-Management-System
│
├── manage.py
├── README.md
│
├── ocms/                     ← MAIN DJANGO PROJECT (configuration only)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── accounts/                 ← Authentication + JWT login
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── courses/                  ← Course system + frontend pages
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   │
│   ├── templates/
│   │   └── courses/
│   │       ├── login.html
│   │       ├── courses.html
│   │       └── admin.html
│   │
│   └── static/
│       └── courses/
│           ├── app.js
│           └── style.css
│
└── staticfiles/              ← auto-created after collectstatic
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone project

```bash
git clone https://github.com/yourusername/ocms.git
cd ocms
```

### 2️⃣ Create virtual environment

```bash
python -m venv env
env\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create admin user

```bash
python manage.py createsuperuser
```

### 6️⃣ Run server

```bash
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---

## 🔑 API Endpoints

| Method | Endpoint              | Description            |
| ------ | --------------------- | ---------------------- |
| POST   | /api/auth/login/      | User login (JWT token) |
| GET    | /api/courses/         | List all courses       |
| POST   | /api/enroll/          | Enroll in course       |
| GET    | /api/admin/analytics/ | Admin analytics        |

---

## 🧠 How It Works

1. User logs in → backend returns JWT token
2. Token stored in browser `localStorage`
3. Frontend sends token in Authorization header
4. Backend validates user
5. User can enroll & access protected APIs

Example header:

```
Authorization: Bearer <token>
```

---

## 📸 Screens

* Login Page
* Courses Page
* Admin Analytics Dashboard

---

## 🛡️ Security

* Password authentication
* JWT protected endpoints
* Token-based authorization
* CSRF safe (API-based)

---

## 📌 Future Improvements

* Course video streaming
* Payment integration
* Email notifications
* Password reset
* User profile page

---

## 👨‍💻 Author

**Aditya Kumar**

B.Tech Computer Science
Online Course Management System Project

---

## 📜 License

This project is for academic/educational use.
