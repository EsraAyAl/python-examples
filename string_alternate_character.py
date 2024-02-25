#This program makes each alternate character into an upper case character and each other alternate character a lower case character.
sentence="Thank you so much for everything"
new_sentence=""
for i in range(len(sentence)):
    if i%2==0:
        new_sentence+=sentence[i].upper() 
    else:
        new_sentence+=sentence[i].lower()
print(new_sentence)

#This program makes each alternate word into an upper case word and each other alternate word into a lower case word.
split_sentence=sentence.split(" ")
new_split_sentence=""
for x in range(len(split_sentence)):
    if x%2==0:
        new_split_sentence+=split_sentence[x].upper() + " "
    else:
        new_split_sentence+=split_sentence[x].lower() + " "
print(new_split_sentence)
    