'''Write a Program to Check Whether a Number is a Palindrome:
Write a program to determine if a number is a palindrome. For example:
○ Input: Enter a number: 121
○ Output: 121 is a palindrome.'''

num = int(input("Enter a number: "))
temp = num
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10
if num == rev:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")

'''OUTPUT:
Enter a number: 161
161 is a palindrome
'''