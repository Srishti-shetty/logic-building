'''Reverse an Array 
Reverse the order of elements in the given array. 
○ Input: [1, 2, 3, 4, 5] 
○ Output: [5, 4, 3, 2, 1] 
'''

n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
print("Original Array:", arr)
arr.reverse()
print("Reversed Array:", arr)

'''OUTPUT:
Enter number of elements: 5
Enter element: 1
Enter element: 2
Enter element: 4
Enter element: 5
Enter element: 6
Original Array: [1, 2, 4, 5, 6]
Reversed Array: [6, 5, 4, 2, 1]'''