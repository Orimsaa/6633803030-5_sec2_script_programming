# ============================================================
# Lab 6.1: Simple Calculator Functions
# ------------------------------------------------------------
# Objective: Define and use functions to perform basic arithmetic
# Challenge: power(base, exponent) with default parameter
# ============================================================

def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

def subtract(a, b):
    """Subtracts second number from first and returns the result."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

def divide(a, b):
    """Divides first number by second. Returns error message if division by zero."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(base, exponent=2):
    """Raises base to the power of exponent. Default exponent is 2 (squaring)."""
    return base ** exponent


while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power (Challenge)")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Exiting calculator. Goodbye!")
        break

    if choice == '1':
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {add(num1, num2)}")
        except ValueError:
            print("Invalid input. Please enter numbers.")

    elif choice == '2':
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {subtract(num1, num2)}")
        except ValueError:
            print("Invalid input. Please enter numbers.")

    elif choice == '3':
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {multiply(num1, num2)}")
        except ValueError:
            print("Invalid input. Please enter numbers.")

    elif choice == '4':
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Result: {divide(num1, num2)}")
        except ValueError:
            print("Invalid input. Please enter numbers.")

    elif choice == '5':
        try:
            num1 = float(input("Enter base number: "))
            exp_input = input("Enter exponent (press Enter for default 2): ")
            if exp_input.strip() == "":
                print(f"Result: {power(num1)}")
            else:
                num2 = float(exp_input)
                print(f"Result: {power(num1, num2)}")
        except ValueError:
            print("Invalid input. Please enter numbers.")

    else:
        print("Invalid choice. Please select from 1-6.")
