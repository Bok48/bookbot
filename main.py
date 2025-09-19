def get_book_text(book):
    with open(f"books/{book}") as f:
        book_text = f.read()
    return book_text

def main():
    book = get_book_text("frankenstein.txt")
    print(f"{book}")

main()