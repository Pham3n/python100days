#Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
characters = ['!', '@', '$', '%', '*']

numofchar = 2
password = ""
passlength = 30 - numofchar
numofnumbers = 5
numnumbers = 0

for passchar in range(1, passlength):
    password += random.choice(letters)
    password += " "

passwordlist = password.split()

if numofnumbers > 0 :
    print("Checking numbers..")
    for number in range(0, numofnumbers) :
        passwordlist[random.randint(0, passlength - 2)] = random.randint(0,10)
    print(f"Added {numofnumbers} numbers\n")
else : print("No numbers..\n")

if numofchar > 0 :
    print("Checking characters..")
    for number in range(0, numofchar) :
        #check if list item is not already assigne a number
        #passwordlist[random.randint(0, passlength - 1)] = random.choice(characters)
        passwordlist.insert(random.randint(1, passlength - 1), random.choice(characters))
    print(f"Added {numofchar} characters\n")
else : print("No characters..\n")

#for letter in password : 
#    if letter.isnumeric() == True :
#        numnumbers += 1

#if numnumbers < numofnumbers :
#    password[random.randint(0, passlength)] = random.choice(numbers)
passwordfinal = ""
#passwordlist = str(passwordlist)
for p in passwordlist :

    passwordfinal += str(p) 

print("Your password is:")
print(passwordfinal)
print(f"It's \"{len(passwordfinal)}\" long")
