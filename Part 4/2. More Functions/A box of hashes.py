def line(times, string):
    first_character = string[0]
    
    print(first_character * times)   


def box_of_hashes(height):
    width = 10
    string = '#'


    while height > 0:
        line(width, string)
        height -= 1



height = 5
box_of_hashes(height)