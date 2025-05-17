from stats import *

def main():
    import sys
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
        list_char_counts = gen_num_char_list(book_path)
        report(list_char_counts=list_char_counts, filepath=book_path)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    print(file_contents)

main()