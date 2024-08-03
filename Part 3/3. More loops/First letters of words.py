sentence = input("Please type in a sentence:")
space = 0

while space != -1:
    first_character = sentence[0]
    print(first_character)
    space = sentence.find(" ")
    sentence = sentence[space + 1:]