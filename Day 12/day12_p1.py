'''Factorial of a Number Using a For Loop:
Write a program to calculate the factorial of a number entered by the user using a
for loop. For example:
○ Input: Enter a number: 4
○ Output: Factorial of 4 is 24.
'''
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("Factorial of", n, "is", fact)

'''OUTPUT:
Enter a number: 6
Factorial of 6 is 720'''