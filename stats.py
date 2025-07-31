def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sorter(items):
    return items["num"]

def report(raw_char):
    report_char = [{"char": each, "num": raw_char[each]} for each in raw_char]
    report_char.sort(reverse=True, key=sorter)
    return report_char