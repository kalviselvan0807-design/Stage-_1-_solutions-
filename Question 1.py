Question 1:
# Simple Calculator 

def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b 
    else:
        return "Invalid Operator"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

# Output
print("Result:", calculator(a, b, op))
