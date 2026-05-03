'''Write a Program to Calculate the Sum of the First N Natural Numbers:
Write a program where the user enters a number N, and the program calculates
the sum of all natural numbers up to N. For example:
○ Input: Enter a number: 5
○ Output: The sum of the first 5 natural numbers is 15.'''

n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("The sum of the first", n, "natural numbers is", total)

'''OUTPUT:
Enter a number: 3
The sum of the first 3 natural numbers is 6
'''