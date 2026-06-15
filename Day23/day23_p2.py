'''Find the Majority Element in an Array 
Find the element that appears more than n/2 times in the array (if any). 
○ Input: [3, 3, 4, 2, 4, 4, 2, 4, 4] 
○ Output: Majority Element: 4 
'''

n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
found = False
for i in arr:
    count = 0
    for j in arr:
        if i == j:
            count += 1
    if count > n // 2:
        print("Majority Element:", i)
        found = True
        break
if found == False:
    print("No Majority Element")

'''OUTPUT:
Enter number of elements: 6
Enter element: 2
Enter element: 3
Enter element: 2
Enter element: 4
Enter element: 2
Enter element: 2
Majority Element: 2'''