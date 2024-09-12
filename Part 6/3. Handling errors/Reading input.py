def read_input(string, lower_limit, upper_limit):
    while True:
        try:
            number = int(input(string))
            if number >= lower_limit and number <= upper_limit:
                return number
        except:
            pass
        print(f"You must type in an integer between {lower_limit} and {upper_limit}")  
    print("You typed in:", number)


if __name__ == "__main__":    
    number = read_input("Please type in a number: ", 5, 10)