import json
import hashlib
import os

USERS_FILE = os.path.join(os.path.dirname(__file__), "users.json")

def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def load_users() -> dict:
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def add_user(username: str, password: str) -> None:
    users = load_users()
    users[username] = _hash_password(password)
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f)


def authenticate(username: str, password: str) -> bool:
    users = load_users()
    hashed = users.get(username)
    if not hashed:
        return False
    return hashed == _hash_password(password)


if __name__ == "__main__":
    import getpass

    user = input("Username: ")
    pwd = getpass.getpass("Password: ")
    if authenticate(user, pwd):
        print("Login successful!")
    else:
        print("Invalid credentials.")
