n = 4
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    for k in range(2 * (n - i)):
        print(" ", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

'''
OUTPUT:
1             1 
1 2         2 1 
1 2 3     3 2 1 
1 2 3 4 4 3 2 1 '''