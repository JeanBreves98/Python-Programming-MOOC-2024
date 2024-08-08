def line(times, string):
    first_character = string[0]
    
    print(first_character * times)   


def square(lenght, string):
    i = lenght
    while i > 0:
        line(lenght, string)
        i -= 1

lenght = 3
string = "o"
square(lenght, string)