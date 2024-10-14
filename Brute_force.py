# Example brute-force attack simulation
import time

#  correct credentials
correct_username = "admin"
correct_password = "password123"

# A list of possible passwords to try in brute force.
password_list = ["123456", "admin", "letmein", "password", "user", "Qwerty", "password123"]


# Simulate brute force
def brute_force(username, password_list):
    for password in password_list:
        print(f"Attempting username: {username} and password: {password}")
        time.sleep(1)  # Simulate time delay for each attempt
        if username == correct_username and password == correct_password:
            print(f"Success! Correct credentials found: {username}/{password}")
            return True
        else:
            print("Incorrect credentials!")
    print("Brute-force attack failed! No correct credentials found.")
    return False


# Start brute-force simulation
brute_force("admin", password_list)
