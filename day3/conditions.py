
bill = 0
print("Welcome to the Rollecoster game")
height=float(input("What is your height?"))

if height>1:
    print("You may continue")
    age=int(input("How old are you?"))
    if age<=12:
        print(f"Pay R{bill} into machine to play")
        bill = 12
    elif age > 12 & age < 18:
        bill = 16 
        print(f"Your ticket will cost R{bill}")
    else:
        bill = 20
        print(f"Youre adult, so pay R{bill} into machine")
    photo = input("Will you be taking photos? YES or NO")
    if photo == "YES"  : 
        bill += 3
        print("That will cost you another R3")
else:print("Youre too short")#| photo == "yes" | photo == "y" | photo == "Y"#