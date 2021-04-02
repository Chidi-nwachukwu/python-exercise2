# Write a function that takes a list of words (strings).
# It should return a tuple containing three integers,
# representing the length of the shortest word, the length
# of the longest word, and the average word length.

import statistics as st

word_list =["chidiebere", "chinonso", "kelechi"]

def find_shortest_word(word_list):
    new_list = []

    new_list = [len(word) for word in word_list]
    new_list.sort()
    return  f"max length:{max(new_list)}, min length: {min(new_list)}, average length: {st.median(new_list)}"


print(find_shortest_word(word_list))