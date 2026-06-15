'''Move Zeros to the End of an Array ○ Move all zeros in the array to the end while maintaining the relative order of non-zero elements. 
○ Input: [0, 1, 2, 0, 3, 4, 0]
○ Output: [1, 2, 3, 4, 0, 0, 0] '''

n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
result = []
for i in arr:
    if i != 0:
        result.append(i)
for i in arr:
    if i == 0:
        result.append(i)
print("Array after moving zeros:", result)

'''OUTPUT:
Enter number of elements: 5
Enter element: 0
Enter element: 8
Enter element: 9
Enter element: 0
Enter element: 7
Array after moving zeros: [8, 9, 7, 0, 0]'''