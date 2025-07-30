def get_book_text(fpath):
    with open(fpath) as f:
        return f.read()
    
def word_count(fpath):
    with open(fpath) as f:
        text = f.read()
    words = text.split()
    return str(len(words))