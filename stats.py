def get_book_text(fpath):
    with open(fpath) as f:
        return f.read()
    
def word_count(fpath):
    with open(fpath) as f:
        text = f.read()
    words = text.split()
    return str(len(words))

def char_count(fpath):
    with open(fpath) as f:
        text = f.read()
        make_lower = text.lower()
        chars = list(make_lower)
        counter = {}
        for each in chars:
            if each in counter:
                counter[each] += 1
            else:
                counter[each] = 1
    return counter