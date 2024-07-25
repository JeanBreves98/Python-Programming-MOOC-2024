num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
operation = input("Operation:")

if operation == "add":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "multiply":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "subtract":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")