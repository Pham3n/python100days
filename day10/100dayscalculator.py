# Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

for operation in operations :
    print(operation)

operation = input('Pick an operation from above: ')

calculator = operations[operation]
answer = calculator(num1, num2) #answer = operations[operation](num1, num2) and remove line above

print(f"{num1} {operation} {num2} = {answer}")
