def main():
        book_path = "books/frankenstein.txt"
        book = get_book(book_path)
        letters = get_letter_count(book)
        print(get_word_count(book))
        for letter in letters:
            print(letter)

def get_book(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)


def get_letter_count(book):
    book_low = book.lower()
    letter_counts = {}
    for letter in book_low:
        if letter in letter_counts:
            letter_counts[letter] += 1
        elif letter.isalpha():
            letter_counts[letter] = 1
    return convert_to_sorted_dic_ls(letter_counts)

def convert_to_sorted_dic_ls(dic):
    ls = []
    for letter in dic:
        entry = {"letter": letter, "count": dic[letter]}
        ls.append(entry)
    ls.sort(reverse=True, key=get_count)
    return ls

def get_count(letter):
    return letter["count"]

main()