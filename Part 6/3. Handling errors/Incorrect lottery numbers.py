def read_file():
    lottery = {}

    with open("lottery_numbers.csv") as lottery_numbers:
        for line in lottery_numbers:
            line = line.strip().split(";")
            week = line[0]
            numbers = line[1].split(",")

            if week[4:].strip().isdigit():  # Checks if the week is valid
                valid_numbers = []
                unique_numbers = []

                for number in numbers:
                    try:
                        num = int(number)
                        if num > 0 and num < 40:
                            if num not in unique_numbers:
                                unique_numbers.append(num) 
                                valid_numbers.append(num)

                    except ValueError:
                        pass

                if len(valid_numbers) == 7: # Only creates a dictionary entry for values which have a length of 7
                    lottery[week] = valid_numbers
    
    return lottery
            

def filter_incorrect():
    with open("correct_numbers.csv", "w") as correct_numbers:
        lottery = read_file()
        for week, numbers in lottery.items():
            numbers_str = ""
            for num in numbers: # Turns the number list into a string
                if numbers_str:
                    numbers_str += ","  # Append a comma before adding the next number
                numbers_str += str(num)  # Convert each number to a string and append it
            
            correct_numbers.write(f"{week};{numbers_str}\n")


if __name__ == "__main__":
    filter_incorrect()