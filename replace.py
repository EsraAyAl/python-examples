#This program makes the sentence replaced

sentence="The!quick!brown!fox!jumps!over!the!lazy!dog."

#print original sentence
print(sentence) 

#original sentence replaced
sentence=sentence.replace("!", " ")

#print replaced sentence
print(sentence)

#print replaced sentence with uppercase
print(sentence.upper())

#print replaced sentence reversed
print(sentence[::-1])