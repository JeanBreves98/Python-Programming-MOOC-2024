def formatted(my_list):
    new_list = []

    for i in my_list:
        i = f"{i:.2f}" #Formats number to not show more than 2 decimals.
        new_list.append(i)
        
    return new_list


if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)

    print(new_list)