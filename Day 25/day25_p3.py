'''Count Words in a String Count the number of words in a sentence. 
○ Input: "I love programming" 
○ Output: 3 '''

text = input("Enter a sentence: ")
count = 1
for i in text:
    if i == " ":
        count += 1
print("Number of words:", count)

'''OUTPUT:
Enter a sentence: i love python
Number of words: 3'''