def line(times, string):
    first_character = string[0]
    
    print(first_character * times)   


def square(lenght, string):
    maximum_size = lenght
    i = 1
    while i <= maximum_size:
        line(i, string)
        i += 1

lenght = 5
string = "#"
square(lenght, string)