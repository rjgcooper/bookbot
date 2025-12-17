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

def sort_chars(char_count):
    sorted_chars = []
    i = 0
    for c in char_count:
        #print(f"{c} with count {char_count[c]}")
        sorted_chars.append({"char": c, "num": char_count[c]})
        #print(sorted_chars[i])
        i += 1
    sorted_chars.sort(reverse=True, key=sort_on)
    #print(sorted_chars)
    return sorted_chars

def sort_on(items):
        return items["num"]


