'''Calculate the Sum of Digits of a Given Number:
Write a program that calculates the sum of the digits of a number entered by the
user. For example:
○ Input: Enter a number: 1234
○ Output: Sum of digits: 10'''

num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print("Sum of digits:", sum)