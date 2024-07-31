string = input("Please type in a string:")
second_character = string[1]
second_to_last_character = string[-2]

if second_character == second_to_last_character:
    print("The second and the second to last characters are " + second_character)
else:
    print("The second and the second to last characters are different")