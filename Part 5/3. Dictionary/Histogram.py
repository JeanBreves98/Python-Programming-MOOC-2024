def histogram(string):
    my_dictionary = {}

    for character in string:
        if character not in my_dictionary:
            my_dictionary[character] = 0
        my_dictionary[character] += 1
    
    for character in my_dictionary:
        times = my_dictionary[character]
        stars = times * '*'
        
        print(f"{character} {stars}")

if __name__ == "__main__":
    histogram("abba")
    histogram("statiscally")