text = input("Enter a paragraph: ")

word_list = text.lower().split() #converted in lowercase and then splitted into list for access each word through loop
words_dict = {} #to store words as key and their frequency as values

for i in word_list: 
    if i in words_dict: 
        words_dict[i] = words_dict[i] + 1 # if word reoccurs it increase its frequency(value)
    else:
        words_dict[i] = 1

print("Top 3 words:")
for i in range(3):  
    max_word = ""
    max_count = 0
    for k in words_dict: #loop to access words_dict and find max frequency words
        if words_dict[k] > max_count:
            max_word = k
            max_count = words_dict[k]
    print(max_word, ":", max_count)
    del words_dict[max_word] #already used word marked as 0 so it won't be picked again
