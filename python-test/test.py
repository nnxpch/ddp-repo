# Customer Order Management System
# Step 1 create dictionary to store customer and product data
# Step 2 create main interface for user to select menu and submenu
# Step 3 create function for manupilating product and customer

# Create 'customer' database using dictionary
customer = {
    'customer1': {
        'name': 'John Doe',
        'contact_details': {
            'email': 'john@example.com',
            'phone': '555-1234'
        },
        'order_history': [
            {'order_id': 101, 'product': 'Laptop', 'quantity': 2, 'total_price': 1999.98},
            {'order_id': 102, 'product': 'Mouse', 'quantity': 1, 'total_price': 19.99}
        ]
    },
    'customer2': {
        'name': 'Jane Smith',
        'contact_details': {
            'email': 'jane@example.com',
            'phone': '555-5678'
        },
        'order_history': [
            {'order_id': 103, 'product': 'Smartphone', 'quantity': 1, 'total_price': 499.99},
            {'order_id': 104, 'product': 'Headphones', 'quantity': 2, 'total_price': 159.98}
        ]
    } 
}

# Create 'product' database using dictionary
product = {
    'product1': {'name': 'Laptop', 'price': 999.99, 'quantity': 5},
    'product2': {'name': 'Smartphone', 'price': 499.99, 'quantity': 5},
    'product3': {'name': 'Headphones', 'price': 79.99, 'quantity': 10},
    'product4': {'name': 'Mouse', 'price': 19.99, 'quantity': 10},
    'product5': {'name': 'Printer', 'price': 199.99, 'quantity': 5}
}

# Create main interface with 2 level of menu
def maininterface():
    while True:
        print("Customer Order Management System")
        print("1. Order processing")
        print("2. Customer Management")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            print("1.1 Add product")
            menu_product = input("Enter choice (1.1): ")
            if menu_product == "1.1": return addproduct_interface()
        elif choice == "2":
            print("2.1 Add new customer")
            print("2.2 Display customer data")
            print("2.3 Remove customer data")
            menu_customer = input("Enter choice (2.1/2.2/2.3): ")
            if menu_customer == "2.1": return addcustomer_interface(customer)
            elif menu_customer == "2.2": return displaycustomer(customer)
            elif menu_customer == "2.3": return removecustomer_interface(customer)
        elif choice == "3": 
            print("Exiting Customer Order Management System.")
            break
        else:
            return print("Error! choice cant be selected")
        pass

def addproduct_interface():
    customer_id = input("Enter customer ID: ")
    # if have enough time, product display should be added for the convenient of customer when add products
    product_id = input("Enter product ID to add to order history: ")
    quantity = int(input("Enter quantity: "))
    return addproduct(customer, product, customer_id, product_id, quantity)

# separate function for 'add new customer' input
def addcustomer_interface(customer):
    # Text input for new customer data 
    customer_id = input("Enter customer ID: ")
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone: ")
    # store new customer data in customer_detail list and will pass this to function 'addcustomer'
    customer_detail = {
        'customer_id': customer_id,
        'name': name,
        'email': email,
        'phone': phone
    }
    return customer_detail

# separate function for 'remove customer' input
def removecustomer_interface(customer):
    customer_id = input("Enter customer ID: ")
    return removecustomer(customer, customer_id)

# Order processing function
# Function 1: Adding product to customer's order history
def addproduct(customer, product, customer_id, product_id, quantity):
    # check if the entered customer and product is existed
    if customer_id in customer and product_id in product:
        customer = customer[customer_id]
        product = product[product_id]

        # check if product quantity is more than the input quantity
        if product["quantity"] > quantity:
            order_id = len(customer["order_history"]) + 1
            total_price = product["price"] * quantity
            order = {
                'order_id': order_id,
                'product': product['name'],
                'quantity': quantity,
                'total_price': total_price
            }
            product["quantity"] -= 1
            customer["order_history"].append(order)
            print("Order placed successfully")
        # Error handling not enough quantity
        else: print("Error! not enough quantity in stock")

    # Error handling no entered customer or product
    else: print("Error! customer or product not found")
    

# Customer management function
# Function 1: Adding new customer

# pass customer_detail (new customer data) from function addcustomer_interface
def addcustomer(customer, customer_detail):
    customer_id = customer_detail[customer_id]

    # Error handling: if customer already exist then it shouldn't be added
    if customer_id in customer:
        print("Error! customer data already exist")
    else: 
        newcust = {
            'name': customer_detail["name"],
            'contact_details': { customer_detail["email"], customer_detail["phone"] },
            'order_history': []
        }
    # add 'newcust' to an existing dictionary 'customer' using customer_id as key
    newcust = customer[customer_id]


# 2. Display customer
def displaycustomer(customer):
    for customer_id, customer_details in customer.items():
        print("Customer ID", customer_id)
        print("Name", customer_details["name"])
        print("Contact details", customer_details["contact_details"])

        for order in customer_details["order_history"]:
            print("Order ID", order["order_id"])
            print("Product", order["product"])
            print("Quantity", order["quantity"])
            print("Total price", order["total_price"])

# 3. Remove customer
def removecustomer(customer, customer_id):
    
    # check if customer exist, if exist then it can be deleted
    if customer_id in customer:
        del customer[customer_id]
        print("Customer remove successfully")
    # Error handling, customer is not existed
    else: print("Customer not found")


# Entry point of the program
if __name__ == "__main__":
    maininterface()