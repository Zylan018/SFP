def calculate(number1, operator, number2):
    if operator == "+":
        return number1 + number2
    if operator == "_":
        return number1 - number2
    if operator == "*":
        return number1 * number2

print(calculate(10, "+", 10))  
print(calculate(10, "-", 10))  
print(calculate(10, "*", 10))
