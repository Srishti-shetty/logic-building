#Pattern

n = 5
for i in range(n):
    for j in range(n):
        if j == abs(n // 2 - i) or j == n - 1 - abs(n // 2 - i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

'''OUTPUT:
    *     
  *   *   
*       * 
  *   *   
    *  
'''