class DataRepository:
    def __init__(self):
        # Sample users: an admin and a non-admin
        self.users = {
            'admin': {'password': 'adminpass', 'role': 'admin'},
            'user': {'password': 'userpass', 'role': 'user'}
        }

    def get_user(self, username):
        return self.users.get(username)


class SecureAPI:
    def start(self):
        print("Secure API is now running...")


class InsecureAPI:
    def start(self):
        print("Insecure API is now running...")
        print("No authentication required.")


class API:
    def __init__(self, data_repo):
        self.data_repo = data_repo
        self.current_user = None

    def start(self):
        print("API System")
        while True:
            print("1. Run Secure API\n2. Run Insecure API\n3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.run_secure_api()
            elif choice == '2':
                self.run_insecure_api()
            elif choice == '3':
                break
            else:
                print("Invalid option.")

    def run_secure_api(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = self.data_repo.get_user(username)
        if user and user['password'] == password and user['role'] == 'admin':
            SecureAPI().start()
        else:
            print("Only admin accounts can start the Secure API.")

    def run_insecure_api(self):
        InsecureAPI().start()


# Example usage
if __name__ == "__main__":
    data_repo = DataRepository()
    api_system = API(data_repo)
    api_system.start()
