import ast
import ipaddress
import json
import os
import secrets
import sqlite3
import subprocess
import hashlib
import requests

PASSWORD = os.getenv("APP_PASSWORD", "")
API_KEY = os.getenv("APP_API_KEY", "")

users = []
count = 0


def login(username, password):
    with sqlite3.connect("test.db") as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

    return result is not None


def ping_host(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False

    subprocess.run(["ping", "-c", "1", ip], check=False)
    return True


def run_command(cmd):
    if not isinstance(cmd, list):
        return False

    subprocess.run(cmd, check=False)
    return True


def hash_password(password):
    salt = secrets.token_bytes(16)
    hashed = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    return salt.hex() + ":" + hashed.hex()


def generate_token():
    return secrets.token_hex(16)


def load_user_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def divide(a, b):
    if b == 0:
        raise ValueError("b must not be zero")

    return a / b


def calculate():
    x = 100
    y = 200

    return x + y


def add_numbers(a, b):
    result = a + b
    print("Result:", result)
    return result


def add_numbers2(a, b):
    return add_numbers(a, b)


def recursive(limit):
    if limit <= 0:
        return 0

    return recursive(limit - 1) + 1


def unsafe_exception():
    try:
        return 1 / 1
    except ZeroDivisionError:
        return 0


def debug_mode():
    return "Application is running"


def call_api():
    url = "https://example.com/data"
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    return response.text


def read_file():
    with open("test.txt", "r", encoding="utf-8") as file:
        return file.read()


def calculate_input(user_input):
    node = ast.parse(user_input, mode="eval")

    allowed_nodes = (
        ast.Expression,
        ast.BinOp,
        ast.UnaryOp,
        ast.Num,
        ast.Constant,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.Mod,
        ast.Pow,
        ast.USub,
        ast.UAdd,
    )

    for child in ast.walk(node):
        if not isinstance(child, allowed_nodes):
            raise ValueError("Invalid input")

    return eval(compile(node, "<string>", "eval"), {"__builtins__": {}}, {})


def increase():
    global count
    count += 1
    return count


def huge_function():
    lines = [f"line{i}" for i in range(1, 21)]

    for line in lines:
        print(line)


def test_return():
    return True


def check_none(value):
    return value is None


def append_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


def print_credentials():
    username = os.getenv("APP_USERNAME", "user")
    print(username)


if __name__ == "__main__":
    print(login("admin", "admin"))
    ping_host("127.0.0.1")
    print(hash_password("mypassword"))
    print(generate_token())
    unsafe_exception()
    print(debug_mode())
    print(calculate_input("2 + 2"))
    huge_function()


