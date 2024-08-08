def line(times, string):
    first_character = string[0]
    
    print(first_character * times)   


def square_of_hashes(lenght):
    string = '#'
    i = lenght
    while i > 0:
        line(lenght, string)
        i -= 1


lenght = 5
square_of_hashes(lenght)