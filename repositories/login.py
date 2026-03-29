USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

def login():
    username = input("Username: ")
    password = input("Password: ")

    user = USERS.get(username)

    if user and user["password"] == password:
        print(f"Login successful. Role: {user['role']}")
        return user["role"]

    print("Wrong credentials")
    return None