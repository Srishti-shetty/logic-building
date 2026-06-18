'''Longest Word in a Sentence Find the longest word in a given sentence. 
○ Input: "The quick brown fox" 
○ Output: "quick" '''

text = input("Enter a sentence: ")
words = text.split()
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Longest word:", longest)

'''OUTPUT:
Enter a sentence: i love programming
Longest word: programming'''