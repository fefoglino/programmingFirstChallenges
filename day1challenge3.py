'''
challenge 3

Write a Python program that accepts a word from the user and reverse[s] it.

'''

wordToReverse = input("Enter a word to reverse ")
reversedWord = ""

for i in range(len(wordToReverse)-1, -1, -1): #the loop stops at 0 so use -1 as the stop number https://stackoverflow.com/questions/29292133/how-to-count-down-in-for-loop
    reversedWord = reversedWord + (wordToReverse[i])

print(reversedWord)