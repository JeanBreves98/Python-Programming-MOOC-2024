from datetime import *

def is_it_valid(pic: str):
    nine_digit = []
    day = pic[0:2]
    month = pic[2:4]
    year = pic[4:6]
    century = pic[6]
    personal_identifier = pic[7:10]
    string = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    if century == '+':
        year = "18" + year
    elif century == '-':
        year = "19" + year
    elif century == 'A':
        year = "20" + year

    if len(pic) != 11:
        return False

    try:
        valid_date = datetime(int(year), int(month), int(day))
    except ValueError:
        return False
    
    nine_digit = day + month + year[2:] + personal_identifier
    index = int(nine_digit) % 31

    if pic[-1] == string[index]:
        return True


if __name__ == "__main__":
    is_it_valid("230827-906F")
    is_it_valid("120488+246L")
    is_it_valid("310823A9877")