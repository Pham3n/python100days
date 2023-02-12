#size           S (R15) / M R20) / L (R25)
#peperoni       Y / N (+R2)
#extra cheese   Y / N (+R3)

#final bill

print("Hi! Welcome to PyPizza")

#bill = 0 although I like to init bill, it's extra code
#bill can be initialised within functions and if statements

size = input("Choose pizza size: S, M or L : ")

def pizza(size):

    if size == "S" :
        bill = 15
        print(f"Your current bill is R{bill}")
        peperoni = input("Peperoni? Y or N : ")
        if peperoni == "Y" :
            bill += 2
            print("Well add R2 to your bill.")
            print(f"Your bill is now R{bill}")
        rest(bill)
    elif size == "M" :
        bill = 20
        print(f"Your current bill is R{bill}")
        peperoni = input("Peperoni? Y or N : ")
        if peperoni == "Y" :
            bill += 3
            print("Well add R3 to your bill.")
            print(f"Your bill is now R{bill}")
        rest(bill)
    elif size == "L":
        bill = 25
        print(f"Your current bill is R{bill}")
        peperoni = input("Peperoni? Y or N : ")
        if peperoni == "Y" :
            bill += 3
            print("Well add R3 to your bill.")
            print(f"Your bill is now R{bill}")
        rest(bill)
    else :
        size= input("Please choose a valid pizza size : ")
        pizza(size)


def rest(bill):
    ex_cheese = input("Add extra cheese? Y or N : ")
    if ex_cheese == "Y" : 
        bill = bill + 1
        print("Well add R1 to your bill.")
        print(f"Your bill is now R{bill}")

    print("Calculating final bill..")
    print(f"Your bill is R{bill}. Please pay into machine.")

pizza(size)