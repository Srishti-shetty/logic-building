n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

'''OUTPUT:
Enter number of rows: 6
A B C D E F 
A B C D E 
A B C D 
A B C 
A B 
A '''