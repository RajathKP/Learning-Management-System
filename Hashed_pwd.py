import bcrypt

password = "my_secure_password"
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode(), salt)

print(f"Original password: {password}")
print(f"Hashed password: {hashed_password}")
