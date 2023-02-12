#pick random name fro  given names to pay the bill

import random

#names = input("Enter patrion names, separated by spaces.\n")

#names = names.split()

names = ['Siphamandla', 'Prince', 'Ntombela']

calc = len(names) - 1

num = random.randint(0,calc)

print(f"The bill will be paid by {names[num]}.")