#Hangman

score = 10

word = "phamene"
workingword = []

for w in word:
    workingword += "_"
i = 0
guess = ""
guessed = ""

def printer(workingword):
    printedword = ""
    for x in range(len(workingword)):
        printedword += workingword[x]
    print(printedword)

while score > 0:
    guess = input(f"Score: {score}. Guess letter:\n")
    if len(guess) > 1:
        print("Please enter only one letter at a time")
    #print(guessed.count(guess))
    if guessed.count(guess) < 1:
        guessed += guess
        if word.count(guess) > 0:
            for w in range(0, len(word)):
                if guess == word[w]:
                    workingword[w] = guess
            printer(workingword)
        else : score -= 1
        if workingword.count("_") == 0:
            print("You win!")
            break
    else : print("Youve entered that one. Try again")

if score == 0 : print("You lost")

print(f"Final printout {workingword}")
