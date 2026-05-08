'''Check if an Integer Can Be Expressed as the Sum of Two Prime Numbers:
Write a program to check if a number can be expressed as the sum of two prime
numbers. Print all such combinations. For example:
○ Input: Enter a number: 34
○ Output:
34 = 3 + 31
34 = 5 + 29
34 = 11 + 23
34 = 17 + 17'''

num = int(input("Enter a number: "))
for i in range(2, num):
    prime1 = True
    for j in range(2, i):
        if i % j == 0:
            prime1 = False
            break
    prime2 = True
    for j in range(2, num - i):
        if (num - i) % j == 0:
            prime2 = False
            break
    if prime1 and prime2:
        print(num, "=", i, "+", num - i)