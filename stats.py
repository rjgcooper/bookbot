def word_count(book):
    words = book.split()
    return len(words)

def character_count(book):
    text = book.lower()
    char_count = {}
    for t in text:
        if t in char_count:
            char_count[t] += 1
        else:
            char_count[t] = 1
    return char_count

