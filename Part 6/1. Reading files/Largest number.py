def largest():
    with open("numbers.txt") as file:
        largest = 0
        for number in file:
            number = int(number)
            if number > largest:
                largest = number
    
    return largest


if __name__ == "__main__":
    largest()    
