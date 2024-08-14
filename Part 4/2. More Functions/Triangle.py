def line(times, string):
    if string == "":
        first_character = "*"
    else: 
        first_character = string[0]
    
    print(first_character * times) 


def triangle(lenght):
    string = "#"
    maximum_size = lenght
    i = 1
    while i <= maximum_size:
        line(i, string)
        i += 1

if __name__ == "__main__":
    lenght = 5
    triangle(lenght)