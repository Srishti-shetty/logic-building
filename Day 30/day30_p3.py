'''3. Swap Keys and Values Task: Create a new dictionary where the original keys become values and the original
values become keys (Dictionary Comprehension).
● Input: data = {"name": "John", "age": 25, "city": "New York"}
● Expected Output: {'John': 'name', 25: 'age', 'New York': 'city'}'''

n = int(input("Enter number of items: "))
data = {}
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value
swapped = {v: k for k, v in data.items()}
print("Swapped Dictionary:", swapped)

'''OUTPUT:
Enter number of items: 3
Enter key: name
Enter value: tanvi
Enter key: age
Enter value: 21
Enter key: city
Enter value: puttur
Swapped Dictionary: {'tanvi': 'name', '21': 'age', 'puttur': 'city'}'''