'''Print the Multiplication Table of a Given Number:
Write a program where the user enters a number, and the program prints its
multiplication table. For example:
○ Input: Enter a number: 5
○ Output:
5 x 1 = 5
5 x 2 = 10
5 x 10 = 50'''

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)