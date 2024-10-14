

# Learning Management System (LMS) in Python

###Description.

This Learning Management System (LMS) is a simple command-line application developed in Python. It allows administrators, teachers, and students to interact with the system securely. Users can register, log in, and perform specific tasks based on their roles

### Key Features
* User Registration: Register users with different roles (Admin, Teacher, Student).
* Login: Authenticate users with username and password.
* Role-based Access: Different functionalities based on user roles.
* Secure API: Admin users can start a secure API.

### Prerequisites
* Python 3
* bcrypt library.

### Installing bcrypt:

To install the bcrypt library, run the following command in your terminal:
```
pip install bcrypt
```

### Project Structure

```
- LMS
    -- Application.py
    -- Insecure_api.py
    -- Secure-api.py
    -- Brute_force.py
    -- Api.py
    -- README.md
```
### How to Use the Application
After running the application, you will be prompted with options to register, log in,or exit the application.

### Registration

Select Register to create a new account.
1. Enter a username, password
2. select a role (admin, teacher, or student).

### Login
1. Select Login to log into the system.
2. Enter your username and password.
Based on your role, different options will be displayed (e.g., Admins can start the secure API).
