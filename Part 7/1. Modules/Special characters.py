from string import *


def separate_characters(my_string: str):
    ascii_string = ""
    punctuation_string = ""
    others_string = ""

    for character in my_string:
        if character in ascii_letters:
            ascii_string += character
        elif character in punctuation:
            punctuation_string += character
        else:
            others_string += character
    
    return ascii_string, punctuation_string, others_string


if __name__ == "__main__": 
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
    kekw = separate_characters('a. s, d: f; g* ') 
    print(kekw[0])
    print(kekw[1])
    print(kekw[2])