#/****************************************
#* Student Name: Dustin Nguyen
#* Date Due: 7/17/2024
#* Date Submitted: 7/17/2024
#* Program Name: Knights UsedLaptop
#* Program Description: This program will allow buyers to buy laptops from a certain seller and allow sellers to sell certain laptops they want to sell
#****************************************/

#Define Classes
class User:
    def __init__(self, name, phone, email, username, role):
        self.name = name
        self.phone = phone
        self.email = email
        self.username = username
        self.role = role

class Laptop:
    def __init__(self, item_number, model, manufacturer, price, seller_username, status = "Available"):
        self.item_number = item_number
        self.model = model
        self.manufacturer = manufacturer
        self.price = price
        self.seller_username = seller_username
        self.status = status

users = []
laptops = []

#Define functions/methods
def create_account():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    username = input("Enter username: ")
    role = input("Enter role (Buyer or Seller): ")

    users.append(User(name, phone, email, username, role))
    print("Account created successfully.")

def delete_account(username):
    global users
    for user in users:
        if user.username == username:
            users.remove(user)
            print("Account deleted successfully.")
            return
    print("Account not found.")

#Seller only function/method
def list_laptops(username):
    for user in users:
        if user.username == username and user.role == "Seller":
            item_number = input("Enter item number: ")
            model = input("Enter model: ")
            manufacturer = input("Enter manufacturer: ")
            price = float(input("Enter price: "))
            laptops.append(Laptop(item_number, model, manufacturer, price, username))
            print("Laptop listed successfully.")
            return

#Buyer only function/method
def list_sellers():
    seller_username = input("Enter seller username: ")
    for user in users:
        if user.username == seller_username and user.role == "Seller":
            for laptop in laptops:
                if laptop.seller_username == seller_username:
                    print(f"Item Number: {laptop.item_number}, Model: {laptop.model}, Manufacturer: {laptop.manufacturer}, Price: {laptop.price}, Status: {laptop.status}")
            return
    print("Seller does not exist.")

#Seller only function/method
def delete_laptops(username, item_number):
    for laptop in laptops:
        if laptop.seller_username == username and laptop.item_number == item_number:
            laptops.remove(laptop)
            print("Laptop deleted successfully.")
            return
    print("Laptop not found.")

#Buyer only function/method
def transaction(buyer_username):
    buyer = next((user for user in users if user.username == buyer_username), None)
    total_price = 0
    purchased_laptops = []
    while True:
        item_number = input("Enter item number to buy (or 'done' to finish): ")
        if item_number == 'done':
            break
        laptop = next((laptop for laptop in laptops if laptop.item_number == item_number and laptop.status == "Available"), None)
        if laptop:
            laptop.status = "Sold"
            total_price += laptop.price
            purchased_laptops.append(laptop)
        else:
            print("Laptop not available.")
    print(f"Username: {buyer.username}, Role: {buyer.role}, Name: {buyer.name}")
    for laptop in purchased_laptops:
        print(f"Item Number: {laptop.item_number}, Manufacturer: {laptop.manufacturer}, Model: {laptop.model}, Price: {laptop.price}")
    print(f"Total Price: {total_price}")

def report_user_information():
    for user in users:
        print(f"Name: {user.name}, Phone: {user.phone}, Email: {user.email}, Username: {user.username}, Role: {user.role}")

def report_laptop_information():
    for laptop in laptops:
        print(f"Item Number: {laptop.item_number}, Model: {laptop.model}, Manufacturer: {laptop.manufacturer}, Price: {laptop.price}, Seller: {laptop.seller_username}, Status: {laptop.status}")

#Defining main for the main function to loop if else statements
def main():
    print("Welcome to Knights UsedLaptop")

    while True:
        print("\nOptions: Create Account, Choose Account, Exit")
        option = input("Enter an option: ")

        if option == "Create Account":
            create_account()
        elif option == "Choose Account":
            username = input("Enter username: ")
            user = next((user for user in users if user.username == username), None)
            if user:
                if user.role == "Buyer":
                    while True:
                        print("\nBuyer Options: List Sellers, Report User Information, Report Laptop Information, Exit Account, Delete Account, Exit")
                        buyer_option = input("Enter an option: ")
                        if buyer_option == "List Sellers":
                            list_sellers()
                            buy_option = input("Enter anything to buy or 'exit' to return: ")
                            if buy_option != 'exit':
                                transaction(username)
                        elif buyer_option == "Report User Information":
                            report_user_information()
                        elif buyer_option == "Report Laptop Information":
                            report_laptop_information()
                        elif buyer_option == "Exit Account":
                            break
                        elif buyer_option == "Delete Account":
                            delete_account(username)
                            break
                        elif buyer_option == "Exit":
                            return
                elif user.role == "Seller":
                    while True:
                        print("\nSeller Options: List Laptops, Delete Laptops, Report User Information, Report Laptop Information, Exit Account, Delete Account, Exit")
                        seller_option = input("Enter an option: ")
                        if seller_option == "List Laptops":
                            list_laptops(username)
                        elif seller_option == "Delete Laptops":
                            item_number = input("Enter item number to delete: ")
                            delete_laptops(username, item_number)
                        elif seller_option == "Report User Information":
                            report_user_information()
                        elif seller_option == "Report Laptop Information":
                            report_laptop_information()
                        elif seller_option == "Exit Account":
                            break
                        elif seller_option == "Delete Account":
                            delete_account(username)
                            break
                        elif seller_option == "Exit":
                            return
            else:
                print("No user found.")
        elif option == "Exit":
            break

if __name__ == "__main__":
    main()
