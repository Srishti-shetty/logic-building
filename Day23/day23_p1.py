'''Find the Missing Number in an Array 
Given an array of numbers from 1 to n with one number missing, find the missing number. 
○ Input: [1, 2, 4, 5, 6] 
○ Output: Missing Number: 3 
'''

n = int(input("Enter value of n: "))
arr = []
for i in range(n - 1):
    num = int(input("Enter element: "))
    arr.append(num)
for i in range(1, n + 1):
    if i not in arr:
        print("Missing Number:", i)
        break

'''OUTPUT:
Enter value of n: 4
Enter element: 1
Enter element: 2
Enter element: 4
Missing Number: 3
'''