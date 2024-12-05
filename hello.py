# Basic Calculator Program

# Function to perform the calculation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:  # Avoid division by zero
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

# Get user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation
    result = calculate(num1, num2, operation)

    # Display the result
    if isinstance(result, str):
        print(result)  # Print error or invalid operation message
    else:
        print(f"{num1} {operation} {num2} = {result}")
except ValueError:
    print("Invalid input. Please enter numeric values for numbers.")
