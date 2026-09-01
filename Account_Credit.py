import json
import os
import random
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
    import main

    data = load_data_credit()
    data_user = main.load_session_user()
    while True:
        try:
            username = input("Please enter your username: ").strip()
            break
        except ValueError:
            print("Error: Please enter a valid username")
            continue
    while True:
        try:
            password = int(input("Please enter a 4-digit PIN: "))
            if len(str(password)) != 4:
                print("Error: PIN must be exactly 4 digits")
                continue
            break
        except ValueError:
            print("Error: Please enter numbers only")
            continue

    created_number_CreditCard = random.randint(10000000000000, 99999999999999)
    created_at = datetime.now().strftime("%b-%Y-%d %H:%M:%S")
    new_id = data_user["id"]
    dis_ar = any(id_te["id"] == new_id for id_te in data)
    if dis_ar:
        print(f"Error: A credit account for this user already exists.")

    for i in data_user:
        new_viza = {
            "id": new_id,
            "Username": username,
            "Password": password,
            "number_ID": created_number_CreditCard,
            "Amount": 0,
            "History": [],
            "Created_at": created_at
        }

    data.append(new_viza)
    save_data_credit(data)
    print("Done: Credit account created successfully")

def login():
    log_file = load_data_credit()
    while True:
        try:
            password = int(input("Please enter your 4-digit PIN: "))
            if len(str(password)) != 4:
                print("Error: PIN must be exactly 4 digits")
                continue
            break
        except ValueError:
            print("Error: Please enter numbers only")
            continue

    found = False
    for index in log_file:
        if password == index["Password"]:
            found = True
            created_at = datetime.now().strftime("%b-%Y-%d %H:%M:%S")
            new_session = {
                "id": index["id"],
                "Number ID": index["number_ID"],
                "Amount": 0,
                "History": [],
                "Created_at": created_at
            }
            save_data_session(new_session)
            print("Done: Login successful, welcome!")
            break

    if not found:
        print("Error: PIN not found")

def deposit():
    data_credit = load_data_credit()
    data_session_file = load_data_session()
    Balance = data_session_file["Amount"]
    History = data_session_file["History"]
    for amount in data_credit:
        if amount["id"] == data_session_file["id"]:
            while True:
                try:
                    Amount_input = float(input("Please enter deposit amount: "))
                    break
                except ValueError:
                    print("Error: Please enter a valid amount")
                    continue

            if Amount_input > 0:
                Balance += Amount_input
                History.append(Amount_input)
                created_at = datetime.now().strftime("%b-%Y-%d %H:%M:%S")
                for key_ed_data in data_credit:
                    Edit_Credit = {
                        "id": key_ed_data["id"],
                        "Number ID": key_ed_data["number_ID"],
                        "Amount": Balance,
                        "History": History,
                        "Created_at": created_at
                    }

                save_data_session(Edit_Credit)
                print(f"Done: Deposited {Amount_input:.2f} EGP, new balance: {Balance:.2f} EGP")
                break
            else:
                print("Error: Deposit amount must be greater than zero")

def show_menu():
    print("==== Credit ====")
    print("1. Create account")
    print("2. Login")
    print("3. Deposit")
    print("0. Exit")

def main():
    while True:
        show_menu()
        while True:
            try:
                choose = int(input("Please Choose Menu: "))
                break
            except ValueError:
                print("Error: Please enter a valid menu number")
                continue
        if choose == 1:
            created_account()
        elif choose == 2:
            login()
        elif choose == 3:
            deposit()
        elif choose == 0:
            break
        else:
            print("Thank you, goodbye!")
            break

if __name__ == "__Account_Credit__":
    main()