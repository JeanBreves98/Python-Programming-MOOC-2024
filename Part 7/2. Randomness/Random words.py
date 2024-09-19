from random import *

def words(n: int, beginning: str):
    words = []
    eligible = []
    return_list = []

    with open("words.txt") as words_file:
        for line in words_file:
            line = line.replace("\n", "")
            words.append(line)  # Appends each word in word list to a list of words
    
    for word in words:
        if word.startswith(beginning) == True:
            eligible.append(word)
    
    if len(eligible) < n:
        raise ValueError
    
    for i in range(n):
        selected = choice(eligible)
        return_list.append(selected)
        eligible.remove(selected)
    
    return return_list


if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)