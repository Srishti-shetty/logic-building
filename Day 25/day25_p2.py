'''Check Palindrome Determine if a string reads the same backward as forward. 
○ Input: "madam" 
○ Output: "Palindrome" 
'''
text = input("Enter a string: ")
reverse = ""
for i in text:
    reverse = i + reverse
if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

'''OUTPUT:
Enter a string: mom
Palindrome
Enter a string: palindrome
Not Palindrome'''