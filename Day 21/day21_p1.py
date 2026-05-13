'''Perfect Number Write a program to determine if a number is a perfect number.
Input: number = 6
Output: Perfect Number
Explanation: 6 is a perfect number because its divisors (1, 2, 3) sum up to 6'''

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")

'''OUTPUT:
Enter a number: 28
28 is a Perfect Number
'''