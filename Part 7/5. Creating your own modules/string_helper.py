from string import ascii_letters, digits

def change_case(orig_string: str):
    new_string = ""

    for character in orig_string:
        if character.islower():
            new_string += character.upper()
        elif character.isupper():
            new_string += character.lower()
        else:
            new_string += character

    return new_string


def split_in_half(orig_string: str):
    length = len(orig_string)
    first_half = orig_string[0:length // 2]
    second_half = orig_string[length // 2: length]

    return (first_half, second_half)

def remove_special_characters(orig_string: str):
    new_string = orig_string

    for character in orig_string:
        if character not in ascii_letters and character not in digits and not character.isspace():
            new_string = new_string.replace(character, "")

    return new_string


'''if __name__ == "__main__":   # Main isn't executed
    my_string = "Well hello there!"
    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)
    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)'''