def line(times, string):
    if string == "":
        first_character = "*"
    else: 
        first_character = string[0]
    
    print(first_character * times)
    

if __name__ == "__main__":    
    line(7, "%")
    line(10, "LOL")
    line(3, "")