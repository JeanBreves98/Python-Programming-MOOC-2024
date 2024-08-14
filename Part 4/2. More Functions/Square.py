def line(times, string):
    if string == "":
        first_character = "*"
    else: 
        first_character = string[0]
    
    print(first_character * times) 


def square(lenght, string):
    i = lenght
    while i > 0:
        line(lenght, string)
        i -= 1

if __name__ == "__main__":
    lenght = 3
    string = "o"
    square(lenght, string)