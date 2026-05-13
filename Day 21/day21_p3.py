'''Sum of the series of n terms Write a program to calculate the sum of the series 1 + 1/2 + 1/3 + ... +
1/n up to the nth term.
Input: n = 4
Output: 2.083333'''

n = int(input("Enter value of n: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + (1 / i)
print("Sum of series =", sum)

'''OUTPUT:
Enter value of n: 6
Sum of series = 2.4499999999999997'''