text = input("Write text:")
original_text = text
text = text.lower()
words = text.split(" ")
correct_words = []

with open("wordlist.txt") as word_list:
    for line in word_list:
        line = line.replace("\n", "")
        correct_words.append(line)  # Appends each word in word list to a list of correct words

for word in words:  # If any of the words on the text are wrong they will be replaced by their highlighted version
    if word not in correct_words:
        original_text = original_text.replace(word, '*' + word + '*')

print(original_text) # Prints text highlighting the wrong words