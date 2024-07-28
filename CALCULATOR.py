def add(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2

def subtract(num1, num2):
    """Return the difference of two numbers."""
    return num1 - num2

def multiply(num1, num2):
    """Return the product of two numbers."""
    return num1 * num2

def divide(num1, num2):
    """Return the quotient of two numbers."""
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return num1 / num2

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Operation choices:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice (1/2/3/4): "))
    if choice == 1:
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == 2:
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == 3:
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == 4:
        try:
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        except ZeroDivisionError as e:
            print(str(e))
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
