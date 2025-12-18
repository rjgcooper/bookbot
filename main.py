from stats import word_count, character_count, sort_chars

def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    char_dic = character_count(book_text)
    sorted_chars = sort_chars(char_dic)
    print_report(book_path, num_words, sorted_chars)

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, num_words, sorted_chars):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")    
    print(f"--------- Character Count -------")
    for c in sorted_chars:
        if c["char"].isalpha():
            print(f"{c["char"]}: {c["num"]}")

    print(f"============= END ===============")

main()