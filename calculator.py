import math

# Function definitions
def add(x, y): 
    return x + y

def subtract(x, y): 
    return x - y

def multiply(x, y): 
    return x * y

def divide(x, y): 
    if y != 0:
        return x / y
    else:
        return "Undefined (division by zero)"

def square(x):
    return x * x

def cube(x):
    return x * x * x

def squareroot(x):
    if x >= 0:
        return x ** (1/2)
    else:
        return "Undefined (square root of negative number)"

def exponent(x, y):
    return x ** y

def remainder(x, y):
    if y != 0:
        return x % y
    else:
        return "Undefined (division by zero)"

# Menu loop
while True:
    print("\n ========== Simple Calculator Menu ========== ")
    print("1. Addition (x + y)")
    print("2. Subtraction (x - y)")
    print("3. Multiplication (x * y)")
    print("4. Division (dividend / divisor)")
    print("5. Square (x^2)")
    print("6. Cube (x^3)")
    print("7. Square Root (√x)")
    print("8. Exponentiation (base ^ exponent)")
    print("9. Remainder (dividend % divisor)")
    print("0. Exit")

    choice = input("Enter your choice (0-9): ")

    if choice == '0':
        print("You are leaving........")
        print("Thank you for using the calculator.")
        break

    elif choice in ['1', '2', '3']:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if choice == '1':
            print(f"Result: {add(x, y)}")
        elif choice == '2':
            print(f"Result: {subtract(x, y)}")
        elif choice == '3':
            print(f"Result: {multiply(x, y)}")

    elif choice in ['4','9']:
        x = float(input("Enter dividend: "))
        y = float(input("Enter divisor: "))
        if choice == '4':
            print(f"Result: {divide(x, y)}")
        elif choice == '9':
            print(f"Result: {remainder(x,y)}")
    
    elif choice == '8':
        x = float(input("Enter the base number: "))
        y = float(input("Enter the exponent: "))
        print(f"Result: {exponent(x, y)}")


    elif choice in ['5', '6', '7']:
        x = float(input("Enter a number (x): "))

        if choice == '5':
            print(f"Result: {square(x)}")
        elif choice == '6':
            print(f"Result: {cube(x)}")
        elif choice == '7':
            print(f"Result: {squareroot(x)}")

    else:
        print("Invalid choice. Please select a number from 0 to 9.")

