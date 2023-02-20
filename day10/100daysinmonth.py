#Check if an input year is a leap year
#Leap years are (1) divisible by 4, (2) not divisible by 100, (3) unless 2 is also divisible by 400

year = int(input("Enter year: "))
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
        if year2 != 0 : return True #print("This is definitely a leap year")
        elif year2 == 0 & year3 == 0 : return True #print("Hm.. It's a leap year, yeah")
        else : print("That might be a leap year, I dont know")
    else :  return False #print("That's not a leap year dog!")

# leapyear(year)

def daysinmonth(year, month):
    """Returns int, number of months in given month and year"""
    #Docstring
    months = {
        "January" : 1,
        "February" : 2,
        "March" : 3,
        "April" : 4,
        "May" : 5,
        "June" : 6,
        "July" : 7,
        "August" : 8,
        "September" : 9,
        "October" : 10,
        "November" : 11,
        "December" : 12
    }
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = days[months[month]-1]
    if leapyear(year) :
        answer += 1
    return answer

month = input("Enter month: ")
days = daysinmonth(year, month)
print(days)