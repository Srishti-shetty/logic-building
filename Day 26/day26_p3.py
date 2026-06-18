'''Find All Substrings of a String Print all possible substrings of a string. 
○ Input: "abc" 
○ Output: ["a", "b", "c", "ab", "bc", "abc"] 
'''
text = input("Enter a string: ")
substrings = []
for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        substrings.append(text[i:j])
print(substrings)

'''OUTPUT:
Enter a string: abcd
['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
'''