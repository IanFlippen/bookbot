from stats import word_count

def main():
    read_Book = word_count('./books/frankenstein.txt')
    print(read_Book + " words found in the document")

main()