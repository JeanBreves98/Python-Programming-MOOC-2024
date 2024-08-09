def first_word(sentence):
    index = sentence.find(space)
    sentence = sentence[0:index]
    return sentence
    
def second_word(sentence):
    index = sentence.find(space)
    sentence = sentence[index + 1:]
    index = sentence.find(space)
    sentence = sentence[0:index]
    return sentence
    
def last_word(sentence):
    while sentence.find(space) != - 1:
        index = sentence.find(space)
        sentence = sentence[index + 1:]
    return sentence    


sentence = "it was a dark and stormy python"
space = " "
word_count = len(sentence.split()) # Maybe it won't be necessary

print(first_word(sentence)) 

print(second_word(sentence)) 
print(last_word(sentence)) #Small error