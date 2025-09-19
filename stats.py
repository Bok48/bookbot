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