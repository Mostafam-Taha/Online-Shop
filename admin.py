import json
import os
from datetime import datetime

data_file_admin = "DataBase/Admin/Admin.json"
data_file_product = "DataBase/Admin/Products.json"
data_file_discount = "DataBase/Admin/Discount.json"

# Load Login
def load_data():
    if not os.path.exists(data_file_admin):
        return []
    with open(data_file_admin, "r", encoding="utf-8") as file:
        return json.load(file)

def save_data(data):
    with open(data_file_admin, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Load Product
def load_product():
    if not os.path.exists(data_file_product):
        return []
    with open(data_file_product, "r", encoding="utf-8") as file:
        return json.load(file)

def save_product(data_product):
    with open(data_file_product, "w", encoding="utf-8") as file:
        json.dump(data_product, file, ensure_ascii=False, indent=4)

# Load Discount
def load_discount():
    if not os.path.exists(data_file_discount):
        return []
    with open(data_file_discount, "r", encoding="utf-8") as file:
        return json.load(file)

def save_discount(data_discount):
    with open(data_file_discount, "w", encoding="utf-8") as file:
        json.dump(data_discount, file, indent=4, ensure_ascii=False)

# ----
def menu_option():
    print("1. Sigh in")
    print("2. Login")
    print("3. App_Product")
    print("4. Discount")
    print("0. Exit")

def option_account():
    while True:
        menu_option()
        while True:
            try:
                user_input = int(input("Please choas From menu: "))
                break
            except ValueError:
                print("Error: Please enter your menu")
                continue

        if user_input == 1:
            sgin_in()
        elif user_input == 2:
            login()
        elif user_input == 3:
            add_product()
        elif user_input == 4:
            discount()
        elif user_input == 0:
            break
        else:
            print("Error: Faild")
            break

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

    while True:
        name_product = input("Please enter your name product: ").strip()
        duplicate = any(row["Name"] == name_product for row in data)
        if duplicate:
            print(f"Error: Product '{name_product}' already exists. Please enter a different name.")
            continue
        break

    while True:
        try:
            price_product = float(input(f"Please enter your price, {name_product}: "))
            break
        except ValueError:
            print("Error: please enter your price currect")
            continue

    while True:
        try:
            quantity = int(input(f"Please enter your quantity, {name_product}: "))
            break
        except ValueError:
            print("Please enter your quantity")
            continue

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
    print(f"{'ID':<5}{'Name':<20}{'Price':<15}{'Qty':<8}{'Created At':<20}")
    print("-" * 68)
    print(f"{id_product:<5}{name_product:<20}{price_product:<15.2f}{quantity:<8}{created_at}")

# Discount
def discount():
    data = load_discount()
    while True:
        try:
            AddDiscount = float(input("Please enter your discount: ").strip())
            NameDiscount = input("Please enter your name discount: ")
            dics = any(dis["Name"] == NameDiscount for dis in data)
            if dics:
                print(f"Error: Product '{NameDiscount}' already exists. Please enter a different name.")
                continue
            break
        except ValueError:
            print("Error: Please enter your discount")
            continue
    new_id = max([emp["id"] for emp in data], default=0) + 1
    created_at = datetime.now().strftime("%b-%Y-%d %H:%M:%S")
    new_input_discount = {
        "id": new_id,
        "Name": NameDiscount,
        "Discount": AddDiscount,
        "Created_at": created_at
    }

    data.append(new_input_discount)
    save_discount(data)
    print("-" * 5)
    print(f"Done: Created discount {AddDiscount}")
