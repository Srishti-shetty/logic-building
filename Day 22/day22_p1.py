'''Print the Array in Sorted Order (Ascending and Descending): 
Write a program to sort an array in ascending and descending order. For example: 
Input: [5, 3, 8, 1] 
Output: 
Ascending: [1, 3, 5, 8] 
Descending: [8, 5, 3, 1]'''

n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
arr.sort()
print("Ascending:", arr)
arr.sort(reverse=True)
print("Descending:", arr)

'''OUTPUT:
Enter number of elements: 2
Enter element: 3 
Enter element: 4
Ascending: [3, 4]
Descending: [4, 3]'''