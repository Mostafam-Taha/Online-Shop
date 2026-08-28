# User
import os
import json
import secrets
import string
from datetime import datetime

data_user_file = "Users.json"
data_session_file = "Session_user.json"

def load_session_user():
    if not os.path.exists(data_user_file):
        return []
    with open(data_session_file, "r", encoding="utf-8") as file:
        return json.load(file)

def save_session_user(data_session):
    with open(data_session_file, "w", encoding="utf-8") as file:
            json.dump(data_session, file, indent=4, ensure_ascii=False)

def load_data():
    if not os.path.exists(data_user_file):
        return []
    with open(data_user_file, "r", encoding="utf-8") as file:
        return json.load(file)

def save_data(data):
    with open(data_user_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def generate_random_string(length=32):
    characters = string.digits + string.ascii_letters + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

class Created_Account:
    def __init__(self, user_admin):
        self.us_ad = user_admin

    def option_adus(self):
        if self.us_ad == "user":
            self.sgin_up()
        elif self.us_ad == "admin":
            pass
        else:
            print("Error")
    
    def sgin_up(self):
        data = load_data()
        data_session = load_session_user()
        print("=" * 20)
        print("Welcome to User")
        print("=" * 20)

        u_username = input("Please enter your username: ")
        while True:
            u_password = input("Please enter your password: ")
            u_password_currunt = input("Please enter your password currunt: ")
            if u_password == u_password_currunt:
                new_id = max([emp["id"] for emp in data], default=0) + 1
                created_at = datetime.now().strftime("%b-%Y-%d %H:%M:%S")
                token_session = generate_random_string()
                # save_session_user(token_session)

                new_account_user = {
                    "id": new_id,
                    "Username": u_username,
                    "Password": u_password,
                    "Token": token_session,
                    "Created_at": created_at
                }

                session_user = {
                    "id": new_id,
                    "Token": token_session,
                    "Created_at": created_at
                }
                data.append(new_account_user)
                save_data(data)

                # Session User
                data_session.append(session_user)
                save_session_user(data_session)
                break
            else:
                print("Error: Incurrect password")
                continue

    def login(self):
        print("-" * 20)
        username = input("Please enter your username: ")
        password = input("please enter your password: ")
        with open(data_user_file, "r", encoding="utf-8") as file:
            file_rearning = json.load(file)
            for i in file_rearning:
                print(i)


                
chease = input("Please Enter your Opint User or admin: ").lower()
Created_Account(chease).login()