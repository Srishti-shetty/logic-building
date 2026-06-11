'''Finding the Longest Sequence of Consecutive 1s in a Binary Array 
Write a program to find the longest sequence of consecutive 1s in a binary array. 
Input: binaryArray = [1, 1, 0, 1, 1, 1] 
Output: 3 '''

n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element (0 or 1): "))
    arr.append(num)
count = 0
max_count = 0
for i in arr:
    if i == 1:
        count += 1
        if count > max_count:
          max_count = count
    else:
        count = 0
print("Longest sequence of consecutive 1s:", max_count)