from difflib import get_close_matches

def dictionary():
    correct_words = []

    with open("wordlist.txt") as word_list:
        for line in word_list:
            line = line.replace("\n", "")
            correct_words.append(line)  # Appends each word in word list to a list of correct words

    return correct_words

def spell_checker(words, correct_words, original_text):
    incorrect_words = []
    highlighted_text = original_text

    for word in words:  # If any of the words on the text are wrong they will be replaced by their highlighted version
        if word not in correct_words:
            highlighted_text = highlighted_text.replace(word, '*' + word + '*')
            incorrect_words.append(word)

    print(highlighted_text) # Prints text highlighting the wrong words

    return incorrect_words


def matches(correct_list, incorrect_list):

    print("suggestions:")
    for incorrect in incorrect_list:
        matching = ", ".join(get_close_matches(incorrect, correct_list))
        print(f"{incorrect}: {matching}")

    return

def main():
    original_text = input("Write text:")
    text = original_text.lower()
    words = text.split(" ")
    correct_list = dictionary()
    incorrect_list = spell_checker(words, correct_list, original_text)
    matches(correct_list, incorrect_list)


main()