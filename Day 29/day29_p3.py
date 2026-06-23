'''Matrix Transpose Find the transpose of a matrix (convert rows to columns and vice versa).
○ Input: A = [[1, 2, 3], [4, 5, 6]]
○ Output: [[1, 4], [2, 5], [3, 6]]'''

rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))
A = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    A.append(row)
transpose = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(A[i][j])
    transpose.append(row)
print("Transpose Matrix:")
for row in transpose:
    print(row)

'''OUTPUT:
Enter rows: 2
Enter columns: 3
1
2
3
4
5
6
Transpose Matrix:
[1, 4]
[2, 5]
[3, 6]'''