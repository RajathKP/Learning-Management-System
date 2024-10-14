class InsecureAPI:
    def start(self):
        print("Insecure API started.")
        print("Warning: Passwords and MFA tokens are not hashed in this mode.")


# Running the application
api = InsecureAPI()
api.start()
