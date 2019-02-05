'''
challenge 4

Write Python program to check the validity of password input by users.
Validation:
-at least 1 letter btwn [a-z] and 1 letter btwn [A-Z]
-at least 1 number btwn [0,9]
-at least 1 character from [$#@]
-minimum 6 characters
-maximum 16 characters

'''
lowercase = False
uppercase = False
number = False
character = False
minLength = False

passwordOk = False


while passwordOk == False:
    password = input("Enter a password ")
    for i in password:
        if i in "abcdefghijklmnopqrstuvwxyz":
            lowercase = True
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase = True
        if i in "0123456789":
            number = True
        if i in "$#@":
            character = True
    if lowercase == True and uppercase == True and number == True and character == True and len(password)<17 and len(password)>5:
        passwordOk = True
        print("Your password is good!")
        break
    print("your password is bad, try again")
    continue