def get_word_count(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    list_words = file_contents.split()
    num_words = len(list_words)
    message = f"{num_words} words found in the document"
    #print(list_words)
    print(message)