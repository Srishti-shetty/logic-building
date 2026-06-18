'''Check if Two Strings are Rotations of Each Other Check if one string is a rotation of another. 
NOTE : the order of characters matters in rotations. 
○ Input: "abcd", "cdab" 
○ Output: "Yes" 
'''

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if len(str1) == len(str2) and str2 in (str1 + str1):
    print("Yes")
else:
    print("No")

'''OUTPUT:
Enter first string: abcd
Enter second string: cdba
No'''