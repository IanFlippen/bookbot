from stats import char_count, word_count

def main():
    split_to_char = char_count('./books/frankenstein.txt')
    print(split_to_char)

main()