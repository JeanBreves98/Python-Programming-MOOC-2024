string = input("Please type in a string:")
desired_lenght = 21
string_lenght = len(string) + 1
filling_characters = desired_lenght - string_lenght
 

print(('*' * filling_characters) + string)