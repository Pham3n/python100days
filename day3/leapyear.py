#Check if an input year is a leap year
#Leap years are (1) divisible by 4, (2) not divisible by 100, (3) unless 2 is also divisible by 400

year = int(input("Enter year:"))
year1 = year%4
year2 = year%100
year3 = year%400

def leapyear(year):
    year1 = year%4
    year2 = year%100
    year3 = year%400
    year = year + 1
    if year1 == 0 :
        print("This coul be a leap year, hold on")
        if year2 != 0 : print("This is definitely a leap year")
        elif year2 == 0 & year3 == 0 : print("Hm.. It's a leap year, yeah")
        else : print("That might be a leap year, I dont know")
    else : print("That's not a leap year dog!")

leapyear(year)

