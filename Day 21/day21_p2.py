'''Largest Prime Factor Write a program to find the largest prime factor of a given number.
Input: number = 28
Output: 7'''

num = int(input("Enter a number: "))
largest = 0
for i in range(2, num + 1):
    if num % i == 0:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            largest = i
print("Largest Prime Factor is:", largest)

'''OUTPUT:
Enter a number: 20
Largest Prime Factor is: 5'''

