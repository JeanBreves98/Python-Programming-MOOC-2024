string = input("Please type in a string:")
character = input("Please type in a character:")
index = string.find(character)
end = index + 3

if end <= len(string):
    print(string[index:end])
