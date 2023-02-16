#Prime number is only devisible by 1 and itself
#1 2 3

number = int(input("Enter number:\n"))
divcount = 0

def primechecker(number, divcount):
    for n in range(2, number):
        if number % n == 0:
            divcount += 1
            # print(f"n = {n}")
            # print(f"divisible {divcount} times")
    if divcount > 0 : print("This is not a prime nummber")
    else : print("That's a prime")

primechecker(number, divcount)


#number must not be divisible by any number between one and itself