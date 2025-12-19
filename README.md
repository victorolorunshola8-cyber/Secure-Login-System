Secure Login System with Role-Based Access Control
Project Overview

This project is a secure web-based authentication system developed using Flask (Python).
It implements secure user registration, login, role-based access control (RBAC), and
multiple security mechanisms to protect against common attacks.

The system was developed as part of a Cybersecurity Internship project by Vault-Tec Security.

Features

Secure user registration with password hashing (bcrypt)

Secure login with credential verification

Login CAPTCHA to prevent automated and brute-force attacks

Role-Based Access Control (Admin & User)

Account lockout after multiple failed login attempts

Session management and logout

SQL Injection protection using ORM (SQLAlchemy)

Input validation and access control

Technologies Used

Python

Flask

Flask-SQLAlchemy

bcrypt

HTML & CSS

SQLite

Project Structure
Secure-Login-System/
│
├── app.py
├── init_db.py
├── database.db
├── templates/
│   ├── login.html
│   └── register.html
├── static/
│   └── style.css
├── screenshots/
├── testing_report.txt
└── README.md

Installation & Setup
1. Clone the Repository
git clone https://github.com/victorolorunshola8-cyber/Secure-Login-System.git
cd Secure-Login-System

2. Install Dependencies
pip install flask flask_sqlalchemy bcrypt

3. Initialize Database
python init_db.py

4. Run the Application
python app.py


Open your browser and visit:

http://127.0.0.1:5000

Security Implementation
Password Hashing

Passwords are hashed using bcrypt before storage to ensure they are never stored in plaintext.

Login CAPTCHA

A CAPTCHA challenge is implemented during login to:

Prevent automated login attempts

Reduce brute-force attacks

Add an extra layer of human verification

Account Lockout

User accounts are automatically locked after three failed login attempts to protect against brute-force attacks.

Role-Based Access Control (RBAC)

Admin users can access the admin dashboard

Regular users are restricted from admin-only functionalities

SQL Injection Prevention

The application uses SQLAlchemy ORM, which safely handles database queries and protects against SQL injection attacks.

Testing

All system features were thoroughly tested, including:

User registration

Login with correct and incorrect credentials

CAPTCHA validation during login

Account lockout after failed attempts

Role-based access restrictions

Session handling and logout

Detailed test results are available in testing_report.txt.

Screenshots

Screenshots demonstrating system functionality are included in the screenshots/ folder:

Registration success

Login with CAPTCHA

Account locked message

Admin dashboard

Access denied message

Author

Name: Olorunshola Peter Victor
Role: Cybersecurity Intern
Project: Secure Login System
Organization: Vault-Tec Security
