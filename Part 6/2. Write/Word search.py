def read_words():
    words = []

    with open("words.txt") as word_list:
        for word in word_list:
            word = word.strip()
            words.append(word)
    
    return words


def find_words(search_term: str):
    matching_words = []
    words = read_words()

    if '.' in search_term:
        for word in words:
            if len(word) == len(search_term):  # Check if the word length matches the search term
                match = True
                for i in range(len(search_term)):  # Compare character by character
                    if search_term[i] != '.' and search_term[i] != word[i]: # If there is a dot it can't be the same word. The same applies if the characters aren't the same on both the searched term and the current word being investigated
                        match = False
                        break
                if match:
                    matching_words.append(word)
    elif '*' in search_term:
        index = search_term.find('*')
        if index == 0:
            search_term = search_term[1:]
            for word in words:
                if word.endswith(search_term) == True:
                    matching_words.append(word)
        elif index == len(search_term) - 1:
            search_term = search_term[:index]
            for word in words:
                if word.startswith(search_term) == True:
                    matching_words.append(word)
    else:
        for word in words:
            if word == search_term:
                    matching_words.append(word)

    return matching_words  


if __name__ == "__main__":
    print(find_words("*vokes"))
    print(find_words("ca."))