'''Matrix Multiplication Multiply two matrices if the number of columns in the first matrix equals the number of rows in the second.
○ Input: A = [[1, 2], [3, 4]], B = [[5, 6], [7, 8]]
○ Output: [[19, 22], [43, 50]]'''

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j] += A[i][k] * B[k][j]
print(result)

'''OUTPUT:
[[19, 22], [43, 50]]'''