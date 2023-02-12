#Love Calculator

#"String".lower -> string
#count() -> the number of times a letter occurs in a string

from operator import countOf


name = input("What is your name?").lower()
name2 = input("What is her name?").lower()

#TRUE
#LOVE

true0 = countOf(name,"t")
true1 = countOf(name,"r")
true2 = countOf(name,"u")
true3 = countOf(name,"e")

love0 = countOf(name,"l")
love1 = countOf(name,"o")
love2 = countOf(name,"v")
love3 = countOf(name,"e")
count = true0+true1+true2+true3+love0+love1+love2+love3
print(count)

true0 = countOf(name2,"t")
true1 = countOf(name2,"r")
true2 = countOf(name2,"u")
true3 = countOf(name2,"e")

love0 = countOf(name2,"l")
love1 = countOf(name2,"o")
love2 = countOf(name2,"v")
love3 = countOf(name2,"e")
count2 = true0+true1+true2+true3+love0+love1+love2+love3
print(count2)

total = count + count2

if total <= 10 and total >= 90 :
    print(f"Your score is {total}%, you're a good match")
elif total >= 40 >= 50 : print(f"Your score is {total}%, youre good toghether.")
elif total > 10 < 90 : print(f"Your score is {total}%")
else : print(f"Your score is {count}{count2}%")
