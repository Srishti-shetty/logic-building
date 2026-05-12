#Pattern

n = 5
for i in range(n):
    ch = ord('E') - i
    for j in range(i + 1):
        print(chr(ch + j), end=" ")
    print()

'''OUTPUT:
E 
D E 
C D E 
B C D E 
A B C D E '''