'''2. Merge Two Dictionaries Task: Combine the items of two dictionaries into a single new dictionary.
● Input:  dict1 = {"name": "John", "age": 25}
          dict2 = {"city": "New York", "country": "USA"}
● Expected Output: {'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA'}'''

n1 = int(input("Enter number of items in first dictionary: "))
dict1 = {}
for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value
n2 = int(input("Enter number of items in second dictionary: "))
dict2 = {}
for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value
dict3 = {}
for k, v in dict1.items():
    dict3[k] = v
for k, v in dict2.items():
    dict3[k] = v
print("Merged Dictionary:", dict3)

'''OUTPUT:Enter number of items in first dictionary: 2
Enter key: name
Enter value: sweedal
Enter key: age
Enter value: 21
Enter number of items in second dictionary: 2
Enter key: city
Enter value: mangalore
Enter key: state
Enter value: karntaka
Merged Dictionary: {'name': 'sweedal', 'age': '21', 'city': 'mangalore', 'state': 'karntaka'}'''