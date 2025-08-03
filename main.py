# main.py

from stats import get_book_text, get_num_words, text_strings, sort_strings
import sys 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    if not text:
        print("Could not read the book file.")
        sys.exit(1)

    word_count = get_num_words(text)

    print("========== BOOKBOT ==========")
    print(f"\nAnalyzing book found at {book_path}...")

    print("\n---------- Word Count ----------")
    print(f'\nFound {word_count} total words')

    char_counts = text_strings(text)
    sorted_chars = sort_strings(char_counts)



    print("\n---------- Character Count ----------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    
    print("\n============== END ================")

if __name__ == "__main__":
    main()