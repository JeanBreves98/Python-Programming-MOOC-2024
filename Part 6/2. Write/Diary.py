def add_an_entry(entry):
    with open("diary.txt", "a") as file:
        file.write(entry + "\n")


def read_entries():
    with open("diary.txt", "r") as file:
        for line in file:
            print(line)

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 1:
        entry = input("Diary entry: ")
        add_an_entry(entry)
        print("Diary saved")
    elif function == 2:
        print("Entries:")
        read_entries()
    elif function == 0:
        break

print("Bye now!")