list = []

print(f"The list is now {list}")

while True:
    option = input("a(d)d, (r)emove or e(x)it:")
    if option == "d":
        if len(list) == 0:  
            list.append(1)
            print(f"The list is now {list}")
        else:
            list.append(list[len(list) - 1] + 1)
            print(f"The list is now {list}")
    elif option == "r":
        list.pop(len(list) - 1)
        print(f"The list is now {list}")
    elif option == "x":
        break

print("Bye!")