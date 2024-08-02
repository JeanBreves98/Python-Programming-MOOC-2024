string = input("Please type in a string:")
character = input("Please type in a character:")
index = 0

while index != - 1:
    start = 0
    string = string[start:]
    index = string.find(character)
    if index == -1:
        break
    end = index + 3
    if end > len(string):
        break
    if end <= len(string):
        print(string[index:end])
        start = index + 1
        string = string[start:]