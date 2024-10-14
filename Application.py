import bcrypt


class DataRepo:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, user_data):
        self.users[user_id] = user_data

    def get_user(self, username):
        for user in self.users.values():
            if user['username'] == username:
                return user
        return None


class Application:
    def __init__(self, data_repo):
        self.data_repo = data_repo
        self.current_user = None

    def start_application(self):
        print("Welcome to the Secure Learning Management System!")
        while True:
            if self.current_user is None:
                print("1. Register\n2. Login\n3. Exit")
                choice = input("Choose an option: ")
                if choice == '1':
                    self.register()
                elif choice == '2':
                    self.login()
                elif choice == '3':
                    break
                else:
                    print("Invalid option. Please try again.")
            else:
                self.dashboard()

    def register(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (admin/teacher/student): ").lower()

        if role not in ['admin', 'teacher', 'student']:
            print("Invalid role. Please enter admin, teacher, or student.")
            return

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        user_id = len(self.data_repo.users) + 1
        self.data_repo.add_user(user_id, {'username': username, 'password': hashed_password, 'role': role})
        print(f"{role.capitalize()} registered successfully!")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = self.data_repo.get_user(username)
        if user and bcrypt.checkpw(password.encode(), user['password']):
            self.current_user = user
            print(f"Login successful! Welcome, {username}.")
        else:
            print("Invalid credentials. Please try again.")
            self.current_user = None

    def dashboard(self):
        if self.current_user['role'] == 'admin':
            print("1. Start Secure API\n2. Logout")
            choice = input("Choose an option: ")
            if choice == '1':
                self.start_secure_api()
            elif choice == '2':
                self.current_user = None
        else:
            print("You are logged in as a non-admin. Restricted access.")
            print("1. Logout")
            choice = input("Choose an option: ")
            if choice == '1':
                self.current_user = None

    def start_secure_api(self):
        print("Starting Secure API...")
        # Secure API logic would go here.
        print("Secure API started successfully.")

# Running the application
data_repo = DataRepo()
app = Application(data_repo)
app.start_application()
