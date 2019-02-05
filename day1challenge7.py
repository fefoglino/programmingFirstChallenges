'''
challenge 7

Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.

'''
listOfNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    print(listOfNumbers)
    print(listOfNumbers[2])
    listOfNumbers.pop(2)
    if len(listOfNumbers)==2:
        break

print(listOfNumbers)
print(listOfNumbers[1])
listOfNumbers.pop(1)

print(listOfNumbers)
print(listOfNumbers[0])
listOfNumbers.pop(0)

print(listOfNumbers)