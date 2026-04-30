n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end=" ")
    print()

'''OUTPUT:
Enter number of rows: 6
          A 
        A B A 
      A B C B A 
    A B C D C B A 
  A B C D E D C B A 
A B C D E F E D C B A 
'''