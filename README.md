# Personal Blog with Flask

A full-featured personal blog website built with Flask featuring user authentication, blog post management, commenting system, and responsive design. This project demonstrates complete web development skills with Python.

## Features
- User registration and authentication
- Create, read, update, delete blog posts
- Comment system
- Responsive Bootstrap design

## Setup Instructions

1. Create virtual environment and install dependencies:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Initialize database:
```bash
flask db init
flask db migrate -m "Initial setup"
flask db upgrade
```

3. Run the application:
```bash
python run.py
```

4. Access at http://localhost:5000
