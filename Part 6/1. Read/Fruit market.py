def read_fruits():
    fruit_dictionary = {}
    with open("fruits.csv") as file:
        for line in file:
            line = line.replace("\n", "")
            parts = line.split(";")
            fruit = parts[0]
            prices = parts[1:]
            for price in prices:
                price = float(price)
            fruit_dictionary[fruit] = price

    return fruit_dictionary


if __name__ == "__main__":
    print(read_fruits())
    