from random import * 
from string import *

def generate_strong_password(length, numbers, special_characters):
    elements = ascii_lowercase
    special = "!?=+-()#"
    password_list = []
    password = ""

    if numbers == True:
        password_list.append(choice(digits))
        elements = elements + digits

    if special_characters == True:
        password_list.append(choice(special))
        elements = elements + special

    for i in range(0, length - len(password_list)):
        password_list.append(choice(elements))

    shuffle(password_list)
    
    for letter in password_list:
        password += letter

    return password


if __name__ == "__main__": 
    for i in range(10):
        print(generate_strong_password(8, True, True))