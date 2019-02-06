'''
Homework for Thurs Feb 7

Converting Celsius/Fahrenheit

'''

def celToFah (celNum):
    return celNum*(9/5) + 32

def fahToCel (fahNum):
    return (fahNum-32) * (5/9)

runProgram = True

while runProgram:
    userChoice = input("Celsius or Fahrenheit? ").lower()
    if  userChoice == "celsius":
        celNum = float(input("Enter temperature "))
        print(celToFah(celNum))
        runProgram = False
        break
    if userChoice == "fahrenheit":
        fahNum = float(input("Enter temperature "))
        print(fahToCel(fahNum))
        runProgram = False
        break
    else:
        continue
        
        