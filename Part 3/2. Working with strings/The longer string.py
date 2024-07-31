string1 = input("Please type in string 1:")
string2 = input("Please type in string 2:")
lenght1 = len(string1)
lenght2 = len(string2)

if lenght1 > lenght2:
    print(string1 + " is longer")
elif lenght1 < lenght2:
    print(string2 + " is longer")
else:
    print("The strings are equally long")