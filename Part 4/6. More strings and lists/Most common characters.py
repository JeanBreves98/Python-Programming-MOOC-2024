def most_common_character(string):
    most_occurences = 0

    for character in string:
        if string.count(character) > most_occurences:
            most_occurences = string.count(character)
            char = character
    
    return char
    

        


if __name__ == "__main__":    
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))