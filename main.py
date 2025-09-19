from stats import count_words
from stats import count_characters

def get_book_text(book):
    with open(f"books/{book}") as f:
        book_text = f.read()
    return book_text

def main():
    book = get_book_text("frankenstein.txt")
    num_words = count_words(book)
    num_chars = count_characters(book)

    print(f"{num_words} words found in the document")
    for char in num_chars:
        print(f"'{char}': {num_chars[char]}")

main()