'''Count Vowels and Consonants Count the number of vowels and consonants in a string.
○ Input: "hello"
○ Output: Vowels: 2, Consonants: 3'''

text = input("Enter a string: ")
vowels = 0
consonants = 0
for ch in text.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)

'''OUTPUT:
Enter a string: hyee
Vowels: 2
Consonants: 2
'''