'''Print a Number in Reverse Order:
Write a program where the user enters a number, and the program prints it in
reverse order. For example:
○ Input: 1234
○ Output: 4321'''

num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reversed number:", rev)