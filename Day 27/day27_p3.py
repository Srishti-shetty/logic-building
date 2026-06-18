'''Remove All Non-Alphabetic Characters Remove all characters that are not letters. 
○ Input: "abc123!@#" 
○ Output: "abc" 
'''

text = input("Enter a string: ")
result = ""
for ch in text:
    if ch.isalpha():
        result += ch
print(result)

'''OUTPUT:
Enter a string: gdhh%$#
gdhh
'''