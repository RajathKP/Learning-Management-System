

# Learning Management System (LMS) in Python

### Description.

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

### Setup and Installation
1. Clone the Repository: Clone this repository to your local machine.

2. Install Dependencies: Install the required Python packages:
```
pip install bcrypt
```
3. Run the Application: Run the application.py file from the terminal or command prompt:
```
python application.py
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

### Admin Features
Admins can start a secure API after logging in.
Admins have access to more options compared to non-admin users.

### Example Output
```
Welcome to the Secure Learning Management System!
1. Register
2. Login
3. Exit
Choose an option: 1
Enter username: Abc
Enter password: Qwerty
Enter role (admin/teacher/student): admin
Admin registered successfully!
1. Register
2. Login
3. Exit
Choose an option: 2
Enter username: Abc
Enter password: Qwerty
Login successful! Welcome, Abc.
1. Start Secure API
2. Logout
Choose an option: 1
Starting Secure API...
Secure API started successfully.
1. Start Secure API
2. Logout

```
