# calculator.py

import math

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
                return "Ошибка: деление на ноль недопустимо."
            return a / b
        elif operator == 'pow':  # возведение в степень
            return math.pow(a, b)
        else:
            return "Ошибка: неподдерживаемая операция для двух чисел."
    except Exception as e:
        return f"Ошибка: {e}"

def single_input_operation(a, operator):
    try:
        if operator == 'sqrt':  # квадратный корень
            if a < 0:
                return "Ошибка: нельзя извлечь корень из отрицательного числа."
            return math.sqrt(a)
        elif operator == 'abs':  # модуль
            return abs(a)
        else:
            return "Ошибка: неподдерживаемая операция для одного числа."
    except Exception as e:
        return f"Ошибка: {e}"

if __name__ == "__main__":
    try:
        operator = input("Введите оператор (+, -, *, /, sqrt, abs, pow): ")

        if operator in ['sqrt', 'abs']:
            a = float(input("Введите число: "))
            result = single_input_operation(a, operator)
        elif operator in ['+', '-', '*', '/', 'pow']:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            result = calculate(a, b, operator)
        else:
            result = "Ошибка: неизвестная операция."

        print("Результат:", result)

    except ValueError:
        print("Ошибка: введите корректные числа.")

