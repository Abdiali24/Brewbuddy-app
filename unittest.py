# Returns the length of the longest words in the list
def length_of_longest_word(list_of_words):
    longest = 0
    for word in list_of_words:
        if len(word) > longest:
            longest = len(word)
    return longest
# Returns the two longest words in the list
def find_two_longest_words(list_of_words):
    sorted_by_length = sorted(list_of_words, key=len)
    return sorted_by_length[:2]
# Returns the dictionary with the key removed
def remove_key_from_dict(a_dict, key):
    if key in a_dict:
        del a_dict[key]
    return a_dict
# Multiples each number in the list by `multiply_by` and adds `add_to` to it
# Returns a new list of the results matching the order of the original list
def mutiply_and_add(list_of_numbers, multiply_by, add_to):
    new = []
    for num in list_of_numbers:
        new.append((num*multiply_by) + add_to)
    return new