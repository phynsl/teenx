# calculator.py

def calculate(a, b, operator):
    try:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                return "Error: Division by zero is not allowed."
            return a / b
        else:
            return "Error: Unsupported operator."
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))

        result = calculate(a, b, operator)
        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers.")
