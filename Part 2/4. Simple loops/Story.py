story = ""
previous_word = ""
while True:
    word = input("Please type in a word:")
    if word == previous_word:
        break
    elif word == "end":
        break
    previous_word = word
    story += word + " "

print(story)