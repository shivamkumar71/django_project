# Shivam Pvt Ltd Django Web Application

**Author:** Shivam Kumar  
**Contact:** deepkumar14379@gmail.com  
**GitHub:** [shivamkumar71](https://github.com/shivamkumar71)

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Setup & Installation](#setup--installation)
5. [App & Module Descriptions](#app--module-descriptions)
6. [Key Models](#key-models)
7. [Key Views & Functionality](#key-views--functionality)
8. [Templates & Static Files](#templates--static-files)
9. [Deployment Guide](#deployment-guide)
10. [Common Issues & Solutions](#common-issues--solutions)
11. [Contributing](#contributing)
12. [License](#license)

---

## 1. Project Overview

This Django project is a personal portfolio and service showcase for Shivam Kumar, a B.Tech student specializing in Artificial Intelligence. The site demonstrates web development, AI, and automation skills, and provides a platform for users to interact, contact, and view services.

---

## 2. Features

- **Home Page:** Gallery and carousel of images (static and from Unsplash API).
- **About Page:** Personal introduction, skills, and mission statement.
- **Services Page:** List of technology and AI services offered.
- **Contact Page:** Contact form for user inquiries.
- **User Authentication:** Registration, login, logout, and dashboard.
- **Dashboard:** User profile management and activity tracking.
- **Admin Panel:** Custom-branded admin interface for site management.
- **Search:** Search functionality for files/content.
- **Responsive Design:** Modern, mobile-friendly UI using Bootstrap.
- **Static & Media Files:** Organized static assets for images and styles.

---

## 3. Project Structure

```
hello/
│
├── db.sqlite3                # SQLite database (local)
├── manage.py                 # Django management script
│
├── hello/                    # Project settings and URLs
│   ├── __init__.py
│   ├── asgi.py
│   ├── contact_data.txt      # (Contact form data, if used)
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
└── home/                     # Main Django app
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations/
    ├── models.py
    ├── static/
    ├── templates/
    ├── tests.py
    ├── urls.py
    └── views.py
```

---

## 4. Setup & Installation

### Prerequisites

- Python 3.8+
- pip
- (Recommended) Virtual environment tool: `venv` or `virtualenv`
- Git

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shivamkumar71/hello.git
   cd hello
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is missing, generate it with `pip freeze > requirements.txt` after installing Django and other packages.)*

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the site:**
   - Home: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 5. App & Module Descriptions

### hello (Project)
- **settings.py:** Main configuration (database, apps, static files, etc.)
- **urls.py:** Root URL routing, includes `home` app URLs and admin.
- **wsgi.py/asgi.py:** Entry points for deployment.

### home (App)
- **models.py:** Database models for Contact, Profile, Activity, etc.
- **views.py:** View functions for all pages and user actions.
- **forms.py:** Django forms for registration, profile editing, etc.
- **templates/:** HTML templates for all pages.
- **static/:** Static assets (images, CSS, JS).
- **urls.py:** App-specific URL routing.

---

## 6. Key Models

**Contact:**  
Stores contact form submissions (name, email, phone, message, date).

**Activity:**  
Tracks user actions (user, action, timestamp, details).

**Profile:**  
(Assumed from code) Stores user profile information.

---

## 7. Key Views & Functionality

- **index:** Home page with image carousel (uses Unsplash API for dynamic images).
- **about:** About page with personal info and skills.
- **services:** Lists services like web/app/AI development, consulting, etc.
- **contact:** Contact form for user inquiries.
- **register/login/logout:** User authentication.
- **dashboard:** User profile and activity log (edit and view modes).
- **search_files:** Search functionality for files/content.
- **admin:** Custom-branded admin interface.

---

## 8. Templates & Static Files

- **Templates:** Located in `home/templates/` (e.g., `index.html`, `about.html`, `services.html`, `contact.html`, `dashboard.html`, `base.html`).
- **Static Files:** Located in `home/static/` (images like `1.jpg.jpg`, `profile.png`, etc.).

---

## 9. Deployment Guide

### Deploying to PythonAnywhere

1. **Push your code to GitHub.**
2. **On PythonAnywhere:**
   - Clone your repo:  
     ```bash
     git clone https://github.com/shivamkumar71/hello.git
     ```
   - Set up a virtual environment and install requirements.
   - Configure the web app (set source directory, WSGI file, static files).
   - Run migrations and create a superuser.
   - Reload the web app from the PythonAnywhere dashboard.

**See earlier messages for a step-by-step PythonAnywhere deployment guide.**

---

## 10. Common Issues & Solutions

- **ModuleNotFoundError: No module named 'django'**
  - Activate your virtual environment and install Django.
- **Static files not loading**
  - Ensure static files are collected and mapped correctly in deployment.
- **Database errors**
  - Run `python manage.py migrate` and check your database settings.

---

## 11. Contributing

1. Fork the repository on GitHub.
2. Clone your fork and create a new branch.
3. Make your changes and commit them.
4. Push to your fork and submit a pull request.

---

## 12. License

This project is for educational and personal portfolio purposes.  
For other uses, please contact the author.

---

**For questions or support, contact:**  
**Email:** deepkumar14379@gmail.com  
**GitHub:** [shivamkumar71](https://github.com/shivamkumar71) 