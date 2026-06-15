'''Find the Second Largest Element in an Array ○ Find the second largest element in the array.
 ○ Input: [10, 20, 4, 45, 99] 
 ○ Output: Second Largest: 45 '''

n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
arr.sort()
print("Second Largest:", arr[-2])

'''OUTPUT:
Enter number of elements: 5
Enter element: 1
Enter element: 2
Enter element: 34
Enter element: 4
Enter element: 87
Second Largest: 34'''