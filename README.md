# Django Car Management System

A complete Django application for car management with authentication, dashboard, and full CRUD operations.

## Features

- User registration, login, and logout
- Secure session-based authentication with Django password hashing
- Add, edit, delete, and list cars
- Protected car management routes (authenticated users only)
- Responsive frontend with HTML, CSS, and JavaScript
- Form validation for user registration and car fields
- Dashboard with navigation

## Tech Stack

- Python 3.12+
- Django 6.0.6
- SQLite (default)

## Project Structure

- `car_management/` - Django project config (`settings.py`, root `urls.py`)
- `cars/` - app with models, forms, views, URLs, admin, tests, migrations
- `templates/` - HTML templates (base, auth, dashboard, car pages)
- `static/` - CSS and JavaScript assets
- `requirements.txt` - dependencies

## Setup Instructions

1. Create and activate virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Create an admin user (optional):
   ```bash
   python manage.py createsuperuser
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```
6. Open in browser:
   - App: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`

## Main Routes

- `/register/` - user registration
- `/login/` - user login
- `/logout/` - user logout
- `/` - dashboard
- `/cars/` - list cars
- `/cars/add/` - add car
- `/cars/<id>/edit/` - update car
- `/cars/<id>/delete/` - delete car

## Testing

Run:

```bash
python manage.py test
```
