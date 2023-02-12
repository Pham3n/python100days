#FizzBuzz
# When number is / 3, FIZZ
# When number is / 5, BUZZ
# When number is / 3 and 5, FIZZbuzz
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, .

shout = 0
f = "Fizz"
b = "Buzz"
fb = "FizzBuzz"

for number in range(1,101):
    if number % 3 == 0 : 
        if number % 5 == 0 :
            shout = fb
        else : shout = f
    elif number % 5 == 0 :
        shout = b
    else : shout = number
    print(shout)

