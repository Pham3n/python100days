#Love Calculator

#"String".lower -> string
#count() -> the number of times a letter occurs in a string

from operator import countOf

name1 = "Angela yu" #input("What is your name?").lower() 11111 = 5
name2 = "Jack Bauer" #input("What is her name?").lower() 111 = 3
name = name1 + name2

#TRUE
#LOVE

true0 = countOf(name,"t")
true1 = countOf(name,"r")
true2 = countOf(name,"u")
true3 = countOf(name,"e")
true = true0+true1+true2+true3

love0 = countOf(name,"l")
love1 = countOf(name,"o")
love2 = countOf(name,"v")
love3 = countOf(name,"e")
love = love0+love1+love2+love3

total =  int(f"{true}{love}")
#print(type(total))
print(f"{total}%")


if total <= 10 or total >= 90 :
    print(f"Your score is {total}%, you're a good match")
elif total >= 40 <= 50 : 
    print(f"Your score is {total}%, youre good toghether.")
elif total > 10 < 90 : 
    print(f"Your score is {total}%")
#else : print(f"Your score is {count}{count2}%")
