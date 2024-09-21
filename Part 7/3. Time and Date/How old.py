from datetime import *

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
born = date(year, month, day)
millennium_eve = date(1999, 12, 31)

if millennium_eve >= born:
    difference = millennium_eve - born
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")