#Nesting list inside other lists

row1 = [" ", " ", " ", " ", " "]
row2 = [" ", " ", " ", " ", " "]
row3 = [" ", " ", " ", " ", " "]
row4 = [" ", " ", " ", " ", " "]
row5 = [" ", " ", " ", " ", " "]

grid = [row1,row2,row3,row4,row5]
ecode = 0
print(f"{grid[0]}\n{grid[1]}\n{grid[2]}\n{grid[3]}\n{grid[4]}")

def ches(grid, ecode):
    if ecode == 1 : print("Please enter valid input")
    input1 = input("Enter 'X' row 1-5. Enter 0 to exit.\n")
    if input1 == "1" : inputrow = int(input1)
    elif input1 == "2" : inputrow = int(input1)
    elif input1 == "3" : inputrow = int(input1)
    elif input1 == "4" : inputrow = int(input1)
    elif input1 == "5" : inputrow = int(input1)
    elif input1 == "C" : exit()
    else : ches(grid, 1)
    input2 = input("Enter 'X' column 1-5. Enter 0 to exit.\n")
    if input2 == "1" : inputcol = int(input2)
    elif input2 == "2" : inputcol = int(input2)
    elif input2 == "3" : inputcol = int(input2)
    elif input2 == "4" : inputcol = int(input2)
    elif input2 == "5" : inputcol = int(input2)
    elif input2 == "C" : exit()
    else : ches(grid, 1)
    #if 0 < input1 <= 5 : inputcol = int(input1)
    #if inputcol or inputrow == 0 : exit()
    grid[inputrow-1][inputcol - 1] = "X"

    printer(grid)



#print(row1)
#print(row2)
#print(row3)
#print(row4)
#print(row5)
def printer(grid):
    print(f"{grid[0]}\n{grid[1]}\n{grid[2]}\n{grid[3]}\n{grid[4]}")
    code = 0
    ches(grid, code)

ches(grid, ecode)