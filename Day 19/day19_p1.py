#Pattern1

n = 5
for i in range(1, n + 1):

    for j in range(i):

        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

'''OUTPUT:
0 
1 0 
0 1 0 
1 0 1 0 
0 1 0 1 0 
'''