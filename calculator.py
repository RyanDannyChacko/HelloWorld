print("Type A for Addition, S for Subtraction, M for Multiplication, and D for Division")
operation = input("Type your letter: ")
first = input("First number: ")
second = input("Second number: ")

if operation == "A":
    add = float(first) + float(second)
    print(f'The sum of {first} and {second} is {add}')

if operation == "a":
    add = float(first) + float(second)
    print(f"The sum of {first} and {second} is {add}")

if operation == "S":
    difference = float(first) - float(second)
    print(f"The difference between {first} and {second} is {difference}")

if operation == "s":
    difference = float(first) - float(second)
    print(f"The difference between {first} and {second} is {difference}")

if operation == "M":
    product = float(first) * float(second)
    print(f"The product of {first} and {second} is {product}")

if operation == "m":
    product = float(first) * float(second)
    print(f"The product of {first} and {second} is {product}")

if operation == "D":
    quotient = float(first) / float(second)
    print(f"The quotient of {first} and {second} is {quotient}")

if operation == "d":
    quotient = float(first) / float(second)
    print(f"The quotient of {first} and {second} is {quotient}")
