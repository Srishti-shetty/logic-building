'''Amstrong Number or Not:
Write a program to check if a number is an Armstrong number. For example:
○ Input: Enter a number: 153
○ Output: 153 is an Armstrong number.'''

num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

'''OUTPUT:
Enter a number: 123
123 is not an Armstrong number
'''