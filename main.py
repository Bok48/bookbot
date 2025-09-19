from stats import (count_words,
                   count_characters, 
                   sort_characters)

def get_book_text(book):
    with open(f"books/{book}") as f:
        book_text = f.read()
    return book_text

def main():
    book = "frankenstein.txt" # Name of text that is being analyzed
                              # placed in books folder

    book_text = get_book_text(book)
    num_words = count_words(book_text)

    # Count and sort characters in book
    num_chars = count_characters(book_text)
    sorted_chars = sort_characters(num_chars)

    # Start of printout
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")

    print("============= END ===============")


main()