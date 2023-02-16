#Ceaser Cipher

upperalphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


#ToDo 1 - Create a function that takes "text" and "shift" as input
# def encode(text:str, shift:int):
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#     workingtext = ""
#     for t in text :
#         #index = letters[]
#         workingtext += letters[letters.index(t) + shift]
#     print(f"the encoded text is: {workingtext}")

# def decode(text:str, shift:int):
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#     workingtext = ""
#     for t in text :
#         #index = letters[]
#         workingtext += letters[letters.index(t) - shift]
#     print(f"the dencoded text is: {workingtext}")

def ceaser(choice, text, shift):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    workingtext = ""

    if shift <= 10 :
        if choice == "decode":
            shift *= -1
        for t in text :
            if letters.count(t) : # if t in letters works as well
                workingtext += letters[letters.index(t) + shift]
            else :
                workingtext += t

        print(f"the {choice}d text is: {workingtext}")
        restart = input("Wanna go again?")
        if restart == "yes" :
            start()
        else : 
            print("Goodbye")

# if shift <= 10 and choice == "encode" :
#     encode(text, shift)
# elif shift <= 10 and choice == "decode" :
#     decode(text, shift)

def start():
    choice = input("Choose 'encode' or 'decode':\n").lower()
    text = input("Enter your text:\n").lower()
    shift = int(input("Chose shift number: 0 - 10\n"))
    
    ceaser(choice, text, shift)

start()