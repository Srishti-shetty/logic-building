'''Write a Program to Find the LCM of Two Numbers:
Write a program where the user enters two numbers, and the program calculates
their least common multiple (LCM). For example:
○ Input: Enter two numbers: 4, 6
○ Output: The LCM of 4 and 6 is 12.
'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
max_num = max(a, b)
while True:
    if max_num % a == 0 and max_num % b == 0:
        print("The LCM of", a, "and", b, "is", max_num)
        break

    max_num += 1

'''OUTPUT:
Enter first number: 6
Enter second number: 8
The LCM of 6 and 8 is 24'''