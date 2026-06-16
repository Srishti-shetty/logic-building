'''Find the Frequency of Each Element in an Array Calculate the frequency of each element in the array. 
○ Input: [1, 2, 2, 3, 1, 4, 5, 1] 
○ Output: {1: 3, 2: 2, 3: 1, 4: 1, 5: 1} 
'''

n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
freq = {}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

'''OUTPUT:
Enter number of elements: 5
Enter element: 3         
Enter element: 4
Enter element: 4
Enter element: 5
Enter element: 6
{3: 1, 4: 2, 5: 1, 6: 1}'''