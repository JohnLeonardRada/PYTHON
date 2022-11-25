# COUNT UNIQUE WORDS
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, "\n")

# TODO: Split verse into list of words
verse_list = verse.split()
print(verse_list, "\n")

# TODO: Print the number of unique words
num_unique = len(set(verse))
print(num_unique, "\n")

# VERSE DICTIONARY
verse_dict = {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, "\n")

# TODO: find the number or uniques keys in the dictionary
num_keys = len(set(verse_dict))
print(num_keys)

# TODO: find whether 'breathe' is a key in the dictionary
contains_breathe = "breath" in verse_dict
print(contains_breathe)

# TODO: create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())
print(sorted_keys)

# TODO: get the first element in the sorted list of keys
print(sorted_keys[0])

# TODO: find the element with the highest value in the list of keys
print(sorted_keys[-1])