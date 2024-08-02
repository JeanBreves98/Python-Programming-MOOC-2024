string = input("Please type in a string:")
lenght = len(string) + 1
a = lenght
b = lenght

while a >= 0:
    print(string[a:b])
    a -= 1