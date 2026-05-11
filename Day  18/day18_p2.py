#Pattern 2
for i in range(2):
    for j in range(10):

        if i == 1 and j >= 4 and j <= 5:
            print(" ", end=" ")
        else:
            print("*", end=" ")

    print()

for i in range(4):
    print("*", end=" ")

    for j in range(10):
        print(" ", end=" ")

    print("*")

for i in range(2):
    for j in range(10):

        if i == 0 and j >= 4 and j <= 5:
            print(" ", end=" ")
        else:
            print("*", end=" ")

    print()

'''OUTPUT:
* * * * * * * * * * 
* * * *     * * * * 
*                     *
*                     *
*                     *
*                     *
* * * *     * * * * 
* * * * * * * * * * 
'''