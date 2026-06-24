'''Dictionary Keys and Values
Task: Extract and print all the keys and values of a dictionary as separate lists.
● Input: data = {"name": "John", "age": 25, "city": "New York"}
● Expected Output: Keys: ["name", "age", "city"], Values: ["John", 25, "New York"]'''

data = {"name": "John", "age": 25, "city": "New York"}
keys = []
values = []
for k, v in data.items():
    keys.append(k)
    values.append(v)
print("Keys:", keys)
print("Values:", values)

'''OUTPUT:
Keys: ['name', 'age', 'city']
Values: ['John', 25, 'New York']'''