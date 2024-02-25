#The variable 'str_manip' stores what the user entered into the box as a string.
str_manip=input("Can you write a sentence please:")
#length of the defined sentence
print(len(str_manip))
#identified last letter of str_manip
last_letter= str_manip[-1]
#print the last letter of the sentence
print(last_letter)
#replace the last letter into @
replace_str_manip= str_manip.replace(last_letter,"@")
#print the replace sentence
print(replace_str_manip)
#print the last 3 characters in str_manip backwards.
print(str_manip[:-3-1:-1])
#defined the five_letters_word
five_letters_word= str_manip[0:3] + str_manip[-2:]
#print the five_letters_word
print(five_letters_word)