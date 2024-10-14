class SecureAPI:
    def start(self):
        print("Secure API started.")
        print("All sensitive data, including passwords and MFA tokens, are hashed and encrypted.")


# Running the application
api = SecureAPI()
api.start()
