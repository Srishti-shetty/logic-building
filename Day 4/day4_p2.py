'''Write a Program to Make a Simple Calculator Using a Switch Case:
Write a program that acts as a calculator, taking two numbers and an operator (+,
-, *, /) from the user, and performing the operation based on the operator. For
example:
○ Input: Enter first number: 10, Operator: +, Second number: 20
○ Output: 10 + 20 = 30'''

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    print(num1, "+", num2, "=", num1 + num2)
elif operator == '-':
    print(num1, "-", num2, "=", num1 - num2)
elif operator == '*':
    print(num1, "*", num2, "=", num1 * num2)
elif operator == '/':
    if num2 != 0:
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid operator")