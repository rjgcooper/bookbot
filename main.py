from stats import word_count, character_count

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = word_count(book_text)
    print(f"Found {num_words} total words")
    print(character_count(book_text))

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

main()