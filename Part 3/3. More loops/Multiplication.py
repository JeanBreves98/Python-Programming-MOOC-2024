number = int(input("Please type in a number:"))
operand1 = 1
operand2 = 1


while operand1 <= number:
    while operand2 <= number:
        result = operand1 * operand2
        print(f"{operand1} x {operand2} = {result}")
        operand2 += 1
    operand2 = 1
    operand1 += 1