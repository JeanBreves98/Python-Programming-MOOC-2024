def invert(dictionary: dict):
    inverted_dictionary = {}

    for key in dictionary:
        value = dictionary[key]
        inverted_dictionary[value] = key

    dictionary.clear()

    for key in inverted_dictionary:
        dictionary[key] = inverted_dictionary[key]

    return dictionary
    

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)