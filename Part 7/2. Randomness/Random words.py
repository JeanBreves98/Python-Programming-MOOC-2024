from random import *

def words(n: int, beginning: str):
    words = []

    with open("words.txt") as words_file:
        for line in words_file:
            line = line.replace("\n", "")
            if line.startswith(beginning):
                words.append(line)  # Appends each word in word list to a list of words
    
    if len(words) < n:
        raise ValueError("Not enough suitable words can be found!")
    
    return sample(words, n)


if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)