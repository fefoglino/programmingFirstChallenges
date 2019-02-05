'''
challenge 6

Write a Python program that accepts a string and calculate the number of digits and letters.

'''
string = input("Enter a string. ")

digits = ""
letters = ""
for i in string:
    if i in "abcdefghijklmnopqrstuvwxyz" or i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letters = letters + i
    elif i in "0123456789":
        digits = digits + i
print("Number of digits in string: ")
print (len(digits))
print("Number of letters in string: ")
print(len(letters))