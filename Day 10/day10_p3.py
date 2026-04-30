#Program to Perform Swapping of Two Numbers:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Before swapping: a =", a, ", b =", b)
temp = a
a = b
b = temp
print("After swapping: a =", a, ", b =", b)

'''OUTPUT:
Enter first number: 5
Enter second number: 10
Before swapping: a = 5 , b = 10
After swapping: a = 10 , b = 5
'''