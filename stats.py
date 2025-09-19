def count_words(text):
    words = text.split()
    return len(words)

# Will count the amount of characters.
# Includes symbols and spaces.
def count_characters(text):
    lowered_text = text.lower()
    char_counter = dict()
    for char in lowered_text:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1
    return char_counter

def get_num(dict):
    return dict["num"]

def sort_characters(chars_dict):
    unsorted_chars_list = list()
    
    for char in chars_dict:
        unsorted_chars_list.append({"char": char, "num": chars_dict[char]})
    unsorted_chars_list.sort(reverse=True, key=get_num)
    return unsorted_chars_list