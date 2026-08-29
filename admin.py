import json
import os
from datetime import datetime

data_file_admin = "Admin.json"
data_file_product = "Products.json"

def load_data():
    if not os.path.exists(data_file_admin):
        return []
    with open(data_file_admin, "r", encoding="utf-8") as file:
        return json.load(file)

def save_data(data):
    with open(data_file_admin, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_product():
    if not os.path.exists(data_file_product):
        return []
    with open(data_file_product, "r", encoding="utf-8") as file:
        return json.load(file)

def save_product(data_product):
    with open(data_file_product, "w", encoding="utf-8") as file:
        json.dump(data_product, file, ensure_ascii=False, indent=4)

def option_account(user_input):
    if user_input == 1:
        sgin_in()
    elif user_input == 2:
        login()
    else:
        print("Error: Faild")

option_user = input("Please choase\n1. Login\n2. Sigh in")

def sgin_in():
    data_admin = load_data()
    print("-"* 20)
    print("Welcome to Admin")
    print("-"* 20)

    username_admin = input("Please enter your username: ")
    while True:
        password_admin = input("Please enter your password: ")
        password_currunt_admin = input("Please enter your password currunt: ")
        if password_admin == password_currunt_admin:
            new_id = max([a_id["id"] for a_id in data_admin], default=0) + 1
            created_at = datetime.now().strftime("%b-%Y-%d %H:%M:%S")
            new_admin_account = {
                "id": new_id,
                "Username": username_admin,
                "Password": password_admin,
                "Created_at": created_at
            }
            data_admin.append(new_admin_account)
            save_data(data_admin)
            print("Done: Created account")
            break
        else:
            print("Error: please enter your password")
            continue

def login():
    print("-"* 20)
    username = input("Please enter your username: ")

    with open(data_file_admin, "r", encoding="utf-8") as file:
        file_admin = json.load(file)
        for index in file_admin:
            if index["Username"] == username:
                add_product()
                break

def add_product():
    data = load_product()
    print("-" * 20)
    name_product = input("Please enter your name product: ")
    price_product = int(input(f"Please enter your price, {name_product}: "))
    quantity = int(input(f"Please enter your quantity, {name_product}: "))
    id_product = max([product_id["id"] for product_id in data], default=0) + 1
    created_at = datetime.now().strftime("%b-%Y-%d %H:%M:%S")
    new_product = {
        "id": id_product,
        "Name": name_product,
        "Price": price_product,
        "quantity": quantity,
        "Created_at": created_at
    }

    data.append(new_product)
    save_product(data)