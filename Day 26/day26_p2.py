'''Find the First Non-Repeating Character Identify the first character that does not repeat in the string. 
○ Input: "swiss" 
○ Output: "w" 
'''

text = input("Enter a string: ")
for ch in text:
    if text.count(ch) == 1:
        print("First Non-Repeating Character:", ch)
        break

'''OUTPUT:
Enter a string: aabbbbcdee 
First Non-Repeating Character: c
'''