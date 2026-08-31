import json
import os
import random
import main
from datetime import datetime

data_Credit_file = "DataBase/Credit/Credit.json"
data_session_file = "DataBase/Credit/Session.json"
data_session_file_main = "DataBase/Users/Session_user.json"
Amount = 0


# Login and Sigh in User
def load_data_credit():
    if not os.path.exists(data_Credit_file):
        return []
    with open(data_Credit_file, "r", encoding="utf-8") as file:
        return json.load(file)

def save_data_credit(data):
    with open(data_Credit_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Session 
def load_data_session():
    if not os.path.exists(data_session_file):
        return []
    with open(data_session_file, "r", encoding="utf-8") as file:
        return json.load(file)

def save_data_session(data_session):
    with open(data_session_file, "w", encoding="utf-8") as file:
        json.dump(data_session, file, ensure_ascii=False, indent=4)

def created_account():
    data = load_data_credit()
    data_user = main.load_session_user()
    while True:
        try:
            username = input("Please enter your username: ").strip()
            break
        except ValueError:
            print("Error: Please enter your username Currect: ")
            continue
    while True:
        try:
            password = int(input("Please enter your password: "))
            if len(str(password)) != 4:
                print("Error: Please enter your password 4 degits")
                continue
            break
        except ValueError:
            print("Error: Please enter your password current")
            continue

    created_number_CreditCard = random.randint(10000000000000, 99999999999999)
    created_at = datetime.now().strftime("%b-%Y-%d %H:%M:%S")

    for i in data_user:
        new_viza = {
            "id": data_user["id"],
            "Username": username,
            "Password": password,
            "number_ID": created_number_CreditCard,
            "Amount": 0,
            "History": [],
            "Created_at": created_at
        }

    data.append(new_viza)
    save_data_credit(data)

def login():
    log_file = load_data_credit()
    while True:
        try:
            password = int(input("Please enter your password: "))
            if len(str(password)) != 4:
                print("Error: Please enter your password 4 degits")
                continue
            break
        except ValueError:
            print("Error: Please enter your password currect")
            continue

    for index in log_file:
        if password == index["Password"]:
            created_at = datetime.now().strftime("%b-%Y-%d %H:%M:%S")
            new_session = {
                "id": index["id"],
                "Number ID": index["number_ID"],
                "Created_at": created_at
            }
    save_data_session(new_session)
    print("Done Welcome to user")
    deposit()

def deposit():
    data_credit = load_data_credit()
    data_session_file = load_data_session()
    for amount in data_credit:
        if amount["id"] == data_session_file:
            print(amount)

deposit()