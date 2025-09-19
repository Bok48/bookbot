from stats import (count_words,
                   count_characters, 
                   sort_characters)
import sys

def get_book_text(book):
    with open(book) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = sys.argv[1] # Path of text that is being analyzed,
                       # placed in books folder

    book_text = get_book_text(book)
    num_words = count_words(book_text)

    # Count and sort characters in book
    num_chars = count_characters(book_text)
    sorted_chars = sort_characters(num_chars)

    # Start of printout
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    # Printing all alphabetical characters in order of most to least used
    for char_dict in sorted_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")

    print("============= END ===============")


main()