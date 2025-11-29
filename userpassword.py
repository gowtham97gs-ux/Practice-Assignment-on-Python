import re

def check_password_strength(password: str) -> bool:
       if len(password) < 9:
        return False
       if not re.search(r"[A-Z]", password):
        return False
       if not re.search(r"[a-z]", password):
        return False
       if not re.search(r"\d", password):
        return False
       if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
       return True
users_db = {}
def register_user():
    print("\n--- User Registration ---")
    username = input("Enter a username: ")
    if username in users_db:
        print("Username already exists. Try another one.")
        return
    password = input("Enter a password: ")
    if not check_password_strength(password):
        print("Weak password. Make sure it has:")
        print("- At least 9 characters")
        print("- Both uppercase and lowercase letters")
        print("- At least one digit (0-9)")
        print("- At least one special character (!, @, #, $, %)")
        return
    confirm_password = input("Re-enter password: ")
    if password != confirm_password:
        print("Passwords do not match. Registration failed.")
        return
    users_db[username] = password
    print(f"User '{username}' registered successfully!")

def login_user():
    print("\n--- User Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users_db and users_db[username] == password:
        print(f"Login successful! Welcome, {username}.")
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
