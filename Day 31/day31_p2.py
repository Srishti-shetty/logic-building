'''2. Power of a Number
Task: Write a recursive function power(base, exponent) to calculate the value of a
base raised to a specific power.
● Input: base = 2, exponent = 3
● Expected Output: 8'''

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print(power(base, exponent))

'''OUTPUT:
Enter base: 5
Enter exponent: 2
25'''