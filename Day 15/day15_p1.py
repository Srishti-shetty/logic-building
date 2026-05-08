'''Check Whether a Number is Prime or Not:
Write a program that checks if a number entered by the user is a prime number.
For example:
○ Input: Enter a number: 17
○ Output: 17 is a prime number.
'''
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

'''OUTPUT:
Enter a number: 31
31 is a prime number
'''