number = 1
factorial = 1

while number > 0:
    number = int(input("Please type in a number:"))
    i = number
    factorial = 1
    while i >= 1:
        factorial *= i
        if i == 1:
            print(f"The factorial of the number {number} is {factorial}")
        i -= 1
print("Thanks and bye!")