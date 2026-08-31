# User
import os
import json
import secrets
import string
import admin
import Account_Credit
from datetime import datetime

result = 0
data_user_file = "DataBase/Users/Users.json"
data_session_file = "DataBase/Users/Session_user.json"
data_products_file = "DataBase/Products/Products.json"
data_Addproduct_file = "DataBase/Products/List_product.json"
data_CheckOut_file = "DataBase/Products/CheckOut.json"
data_session_file_AccountCredit = "DataBase/Credit/Session.json"

# Sessions
def load_session_user():
    if not os.path.exists(data_user_file):
        return []
    with open(data_session_file, "r", encoding="utf-8") as file:
        return json.load(file)

def save_session_user(data_session):
    with open(data_session_file, "w", encoding="utf-8") as file:
            json.dump(data_session, file, indent=4, ensure_ascii=False)

# Login User
def load_data():
    if not os.path.exists(data_user_file):
        return []
    with open(data_user_file, "r", encoding="utf-8") as file:
        return json.load(file)

def save_data(data):
    with open(data_user_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Add Product
def load_AddProduct_data():
    if not os.path.exists(data_Addproduct_file):
        return []
    with open(data_Addproduct_file, "r", encoding="utf-8") as file:
        return json.load(file)

def save_AddProduct_data(data_AddProduct):
    with open(data_Addproduct_file, "w", encoding="utf-8") as file:
        json.dump(data_AddProduct, file, indent=4, ensure_ascii=False)

# CheckOut
def load_CheckOut():
    if not os.path.exists(data_CheckOut_file):
        return []
    with open(data_CheckOut_file, "r", encoding="utf-8") as file:
        return json.load(file)

def save_CheckOut(data_checkout):
    with open(data_CheckOut_file, "w", encoding="utf-8") as file:
        json.dump(data_checkout, file, indent=4, ensure_ascii=False)

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
            admin.option_account()
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
                save_session_user(session_user)
                print("Done: Created account")
                break
            else:
                print("Error: Incurrect password")
                continue

    def login(self):
        print("-" * 20)
        username = input("Please enter your username: ")
        with open(data_user_file, "r", encoding="utf-8") as file:
            file_rearning = json.load(file)

            for i in file_rearning:
                if username == i["Username"]:
                    password = input("Please enter your password: ")
                    if password == i["Password"]:
                        print("Done: Login account")
                        self.products()

class Online_Shop:
    def products(self):
        data = load_AddProduct_data()
        with open(data_products_file, "r", encoding="utf-8") as file, open(data_session_file, "r", encoding="utf-8") as file_user:
            read_all_products = json.load(file)
            read_all_product_user = json.load(file_user)
            
            print(f"{'ID':<5}{'Name':<20}{'Price':<15}{'Qty':<8}{'Created At':<20}")
            print("-" * 68)
            
            for i in read_all_products: 
                print(f"{i['id']:<5}{i['Name']:<20}{i['Price']:<15.2f}{i['quantity']:<8}{i['Created_at']}")

            print("-" * 4)
            while True:
                select_product = input("Please select product: ").strip()
                if select_product == "":
                    print("Error: You must enter a value")
                    continue
                break

            for product in read_all_products:
                if select_product == product["Name"]:
                    add_id = product["id"]
                    add_id_user = read_all_product_user["id"]
                    add_name = product["Name"]
                    add_price = product["Price"]
                    add_token = read_all_product_user["Token"]
                    created_at = datetime.now().strftime("%b-%Y-%d %H:%M:%S")
                    new_add_cart = {
                        "id": add_id,
                        "id_user": add_id_user,
                        "Name": add_name,
                        "Price": add_price,
                        "Token": add_token,
                        "Created_at": created_at
                    }

                    data.append(new_add_cart)
                    save_AddProduct_data(data)
                    
                    print(f"Done: Add to cart {add_name}")
                    break

    def show_all_product(self):
            file_reading = load_AddProduct_data()
            print(f"{'ID':<5}{'Name':<20}{'Price':<15}{'Qty':<8}{'Created At':<20}")
            print("-" * 68)
            for index in file_reading: 
                print(f"{index['id']:<5}{index['Name']:<20}{index['Price']:<15.2f}{index['quantity']:<8}{index['Created_at']}")

    def chack_out(self):
        global result
        data = load_CheckOut()
        file_reading = load_AddProduct_data()
        file_reading_users = load_data()
        file_admin_discount = admin.load_discount()

        # Imported File Account Credit
        data_session_file = Account_Credit.load_data_session()
        data_file_AccountCredit = Account_Credit.load_data_credit()

        # File Credit
        
        def save_data_session(data_session):
            with open(data_session_file_AccountCredit, "w", encoding="utf-8") as file:
                json.dump(data_session, file, ensure_ascii=False, indent=4)

        for index in file_reading_users:
            for kay in file_reading:
                if index["id"] == kay["id_user"]:
                    result = kay["Price"] + result

                    menu = f"{kay['Name']:<20}{kay['Price']:>10.2f} EGP"
                    print(menu)

        print("-" * 32)
        print(f"{'Total':<20}{result:>10.2f} EGP")

        # Discount
        while True:
            quiz = input("Do you add discount (Yas => y, No=> n)? ")
            if quiz == "y":
                en_discount = input("Enter your discount: ")
                search_discount = admin.load_discount()
                result_after_discount = None
                for key_discount in search_discount:
                    if en_discount == key_discount["Name"]:
                        result_after_discount = result - key_discount["Discount"]
                        print(f"{'Total':<20}{result:>10.2f} EGP")
                        print(f"{'Dis':<20} {-key_discount["Discount"]:>10.2f} EGP")
                        print(f"{'Total':<20}{result_after_discount:>10.2f} EGP")
                break
            elif quiz == "n":
                print("Ok")
                result_after_discount = None
                break
            else:
                print("Error: Try agian")
                result_after_discount = None
                continue

        created_at = datetime.now().strftime("%b-%Y-%d %H:%M:%S")
        for add_checkout_index, discount_admin in zip(file_reading, file_admin_discount ):
            add_checkout = {
                "Products": (add_checkout_index["Name"], add_checkout_index["Price"]),
                "Total_price": result,
                "Discount": (discount_admin["Name"], discount_admin["Discount"]),
                "Total_After_discount": result_after_discount,
                "Created_at": created_at
            }

        while True:
            try:
                choose = input("Do you want to complete it? (Yas => y, No => n): ").strip()
                break
            except ValueError:
                print("Error")
                continue

        if data_session_file["Amount"] < result:
            print("You do not h ave enough credit.")
            return
        else:
            if result_after_discount != None:
                Balance = data_session_file["Amount"] - result_after_discount
            else:
                Balance = data_session_file["Amount"] - result
                
        print(f"{Balance} EGP of your account has been deducted.")

        History = data_session_file["History"]
        if choose == "y":
            if result_after_discount != None:
                History.append(result_after_discount * -1)
            else:
                History.append(result * -1)

            for key_ed_data in data_file_AccountCredit:
                Edit_Credit = {
                    "id": key_ed_data["id"],
                    "Number ID": key_ed_data["number_ID"],
                    "Amount": Balance,
                    "History": History,
                    "Created_at": created_at
                }

            save_data_session(Edit_Credit)
            
            data.append(add_checkout)
            save_CheckOut(data)
            print("Done")
        elif choose == "n":
            print("Ok")

def show_LoSi():
    print("1. Sigh in")
    print("2. Login")
    print("3. Show Menu OS")

def show_menu():
    print("1. Products")
    print("2. Show All Product")
    print("3. Check Out")
    print("0. Exit")

def CA_User():
    in_CA = Created_Account()
    while True:
        show_LoSi()
        choose = int(input("Please Choose From Menu: "))


def manu():
    in_OS = Online_Shop()
    while True:
        show_menu()
        choose = int(input("Please Choose from menu: "))
        if choose == 1:
            in_OS.products()
        elif choose == 2:
            in_OS.show_all_product()
        elif choose == 3:
            in_OS.chack_out()
        elif choose == 0:
            break
        else:
            print("Error: Again")
            continue

def InputUser():
    if __name__ == "__main__":
        while True:
            chease = input("Please Enter your Opint User or admin: ").lower()
            if chease == "":
                print("Error: You must enter a value")
                continue
            else:
                Online_Shop().chack_out()
                break
