'''Write a Program to Display All Factors of a Number:
Write a program to find and print all factors of a number entered by the user. For
example:
○ Input: Enter a number: 28
○ Output: Factors of 28: 1, 2, 4, 7, 14, 28
'''
num = int(input("Enter a number: "))
print("Factors of", num, "are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

'''OUTPUT:
Enter a number: 26
Factors of 26 are:
1 2 13 26 
'''