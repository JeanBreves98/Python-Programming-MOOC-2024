number = int(input("Please type in a number:"))
i = 1
x = 2
y = 1

while i <= number:
    if x <= number:
        print(x)
    if y <= number:
        print(y)
    x += 2
    y += 2
    i += 1