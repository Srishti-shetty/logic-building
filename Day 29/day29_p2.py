'''Search an Element in a Matrix Search for a given element in a matrix and return its position.
○ Input:A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
 Target = 5
○ Output: Position: (1, 1) (0-based index)'''

A = []
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A.append(row)
target = int(input("Enter target element: "))
found = False
for i in range(rows):
    for j in range(cols):
        if A[i][j] == target:
            print("Position:", (i, j))
            found = True
if found == False:
    print("Element not found")

'''OUTPUT:
Enter rows: 3
Enter columns: 3
1
2
3
4
5
6
7
8
9
Enter target element: 5
Position: (1, 1)'''