def no_vowels(string):
    new_string = string.replace("a", "")
    new_string = new_string.replace("e", "")
    new_string = new_string.replace("i", "")
    new_string = new_string.replace("o", "")
    new_string = new_string.replace("u", "")

    return new_string


if __name__ == "__main__": 
    my_string = "this is an example"
    print(no_vowels(my_string))