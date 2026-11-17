# Django Authentication System

A simple Django-based authentication system that allows users to register, log in, access protected pages, and log out securely.

## Features

- User Registration
- User Login with Username or Email
- Password Authentication
- Secure Password Hashing using Django's built-in authentication system
- Protected Pages using `@login_required`
- User Logout
- Automatic Redirect for Unauthenticated Users
- Django Session Management

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- Django Built-in User Model

## Project Structure

```text
Django-authentication/
│
├── loginapp/
│   ├── authentication/
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── ...
│   │
│   ├── loginapp/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   │
│   └── manage.py
│
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/gagukibriya/Django-authentication.git
```

### 2. Navigate to the Project Directory

```bash
cd Django-authentication/loginapp
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Authentication Workflow

1. New users can create an account through the registration page.
2. After registration, users are redirected to the login page.
3. Registered users can log in using their username or email and password.
4. Authenticated users can access protected pages.
5. Users can log out to end their authenticated session.
6. Unauthenticated users are redirected to the login page when accessing protected pages.

## Learning Objectives

This project was created to practice:

- Django Authentication
- User Registration and Login
- Django Views and URL Routing
- Session Management
- Authentication Decorators
- Template Rendering and Redirects

## Author

**Kibriya**

GitHub: [@gagukibriya](https://github.com/gagukibriya)

Repository: [Django Authentication](https://github.com/gagukibriya/Django-authentication)