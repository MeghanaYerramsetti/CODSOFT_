def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Welcome to the Simple Calculator!")
    
    while True:
        try:
            # Input numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Input operation
            print("Select operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")

            operation = input("Enter the operation (1/2/3/4) or 'q' to quit: ")

            if operation == 'q':
                print("Exiting the calculator. Goodbye!")
                break

            if operation == '1':
  
