'''Program to Check Whether the Number is Odd or Even:
Write a program that checks whether a number entered by the user is odd or
even. For example:
○ Input: Enter a number: 7
○ Output: 7 is an odd number'''

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")