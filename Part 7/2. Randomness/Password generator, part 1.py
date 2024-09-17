from random import * 
from string import *

def generate_password(length):
    letters = ascii_lowercase
    password_list = []
    password = ""
    
    for i in range(0, length):
        password_list.append(choice(letters))
    
    for letter in password_list:
        password += letter

    return password


if __name__ == "__main__": 
    for i in range(10):
        print(generate_password(8))