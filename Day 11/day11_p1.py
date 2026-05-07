'''Write a Program to Find the Largest Number Among Three Numbers:
Write a program where the user enters three numbers, and the program finds
and displays the largest number among them. For example:
○ Input: Enter three numbers: 12, 25, 7
○ Output: The largest number is: 25'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("The largest number is:", a)
elif b >= a and b >= c:
    print("The largest number is:", b)
else:
    print("The largest number is:", c)

'''OUTPUT:
Enter first number: 25
Enter second number: 60
Enter third number: 21
The largest number is: 60'''