print("Welcome to the calculator application!")

def add(a,b):
    return a + b
def sub(a,b):
    return a-b
def mul(a,b):
    return a * b
def div(a,b):
    return a/b

first_number = int(input("Enter the first number:\t"))
operation = input("Enter which operation you would like to perform:\n+\n-\n*\n\\\n")
second_number = int(input("Enter the second number:\t"))

if operation == "+":
    print(add(first_number,second_number))
elif operation == "-":
    print(sub(first_number,second_number))
elif operation == "*":
    print(mul(first_number,second_number))
elif operation =="\\":
    print(div(first_number,second_number))
else:
    print("Enter the right values, Try again!")