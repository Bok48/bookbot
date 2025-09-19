def get_book_text(book):
    with open(f"books/{book}") as f:
        book_text = f.read()
    return book_text

def count_words(text):
    words = text.split()
    return len(words)

def main():
    book = get_book_text("frankenstein.txt")
    num_words = count_words(book)
    print(f"{num_words} words found in the document")

main()