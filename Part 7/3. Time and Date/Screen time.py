from datetime import *

filename = input("Filename: ")
starting_date  = input("Starting date:")
starting_date = datetime.strptime(starting_date, "%d.%m.%Y")
current_date = starting_date
days_input = int(input("How many days: "))
i = 0
tv_list = []
computer_list = []
mobile_list = []
days_list = []

print("Please type in screen time in minutes on each day (TV computer mobile): ")

while i < days_input:
    tv, computer, mobile = input(f"Screen time {current_date.strftime('%d.%m.%Y')}: ").split()
    tv_list.append(int(tv))
    computer_list.append(int(computer))
    mobile_list.append(int(mobile))
    days_list.append(current_date.strftime('%d.%m.%Y'))
    i += 1
    current_date = current_date + timedelta(days = 1)

tv_total = sum(tv_list)
computer_total = sum(computer_list)
mobile_total = sum(mobile_list)
total = tv_total + computer_total + mobile_total
average = total / days_input
end_date = current_date - timedelta(days=1)

with open(filename, "w") as file:
    file.write(f"Time period: {starting_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\n")
    file.write(f"Total minutes: {total}\n")
    file.write(f"Average minutes: {average:.1f}\n")

    for i in range(days_input):
        file.write(f"{days_list[i]}: {tv_list[i]}/{computer_list[i]}/{mobile_list[i]}\n")