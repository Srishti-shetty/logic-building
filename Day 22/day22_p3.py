'''Finding the Most Frequent Element in an Array 
Write a program to find the most frequent element in an array. 
Input: array = [1, 2, 2, 3, 3, 3] 
Output: 3  
'''

n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
max_count = 0
most_frequent = arr[0]
for i in arr:
    count = arr.count(i)
    if count > max_count:
        max_count = count
        most_frequent = i
print("Most frequent element:", most_frequent)

'''OUTPUT:
Enter number of elements: 4
Enter element: 2
Enter element: 4
Enter element: 3
Enter element: 2
Most frequent element: 2'''