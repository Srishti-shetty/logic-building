'''Write a Program to Calculate the Power of a Number:
Write a program that takes a base and an exponent as input and calculates the
power of the base raised to the exponent using both manual calculation and the
pow() function. For example:
○ Input: Base: 2, Exponent: 3
○ Output:
Result using manual calculation: 8
Result using pow(): 8
'''
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
result = 1
for i in range(exp):
    result = result * base
print("Result using manual calculation:", result)
print("Result using pow():", pow(base, exp))

'''OUTPUT:
Enter base: 3
Enter exponent: 2
Result using manual calculation: 9
Result using pow(): 9'''