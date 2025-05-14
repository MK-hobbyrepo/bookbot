from stats import get_word_count

def main():
    get_word_count("books/frankenstein.txt")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    print(file_contents)

main()