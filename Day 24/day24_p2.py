'''Remove Duplicates from an Array ○ Remove all duplicates from the given array and return the unique elements..
 ○ Input: [1, 2, 2, 3, 4, 1, 5] 
 ○ Output: [1, 2, 3, 4, 5] '''

n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)
print("Array after removing duplicates:", unique)

'''OUTPUT:
Enter number of elements: 4
Enter element: 2
Enter element: 2
Enter element: 3 
Enter element: 4
Array after removing duplicates: [2, 3, 4]'''