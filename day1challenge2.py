'''
challenge 2

Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)

'''

divisible = []

for i in range (1500, 2701):
    if i%5 ==0 and i%7 ==0:
        divisible.append(i)
        
print("Numbers divisible by 5 and 7 btwn 1500 and 2700, inclusive: ")
print(divisible)