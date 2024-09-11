function = -1

def write():
    with open("dictionary.txt", "a") as dictionary:
        dictionary.write(f"{finnish} - {english}\n")


def read(searched_term):
    found = []
    with open("dictionary.txt") as dictionary:
        for line in dictionary:
            if searched_term in line:
                found.append(line)

    return found


while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function:"))
    if function == 1:
        finnish = input("The word in finnish: ")
        english = input("The word in english: ")
        write()
        print("Dictionary entry added")
    elif function == 2:
        searched_term = input("Searched term: ")
        found = read(searched_term)
        for item in found:
            print(item)
    elif function == 3:
        break

print("Bye")