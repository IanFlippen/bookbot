from stats import get_num_words, get_chars_dict, report
import sys

def main():
    try:
        book_path = sys.argv[1]
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted = report(chars_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at "f"{book_path}""...")
    print("----------- Word Count ----------")
    print("Found", num_words, "total words")
    print("--------- Character Count -------")
    for each in sorted:
        if each['char'].isalpha():
            print(f"{each['char']}: {each['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
