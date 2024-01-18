#calculator

def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    if num2 == 0:
        return "Error: Cant divide by zero"
    else: return num1 / num2

def calculator():
    print("Select an operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter operation choice: ")

    if choice == "1":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print("Result: ", add(num1, num2))
    elif choice == "2":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print("Result: ", subtract(num1, num2))
    elif choice == "3":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print("Result: ", multiply(num1, num2))
    elif choice == "4":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print("Result: ", divide(num1, num2))
    else: print("Error! no selected operation")
    
calculator()

