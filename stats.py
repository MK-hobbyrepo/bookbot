def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    list_words = file_contents.split()
    num_words = len(list_words)
    message = f"Found {num_words} total words"
    #print(list_words)
    print(message)

def get_num_chars(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    #file contents is a string
    char_dict = {}
    chars = list(file_contents)
    for char in chars:
        char = char.lower()
        if char in char_dict.keys():
            #key exists
            char_dict[char] += 1
        else:
            #init key
            char_dict[char] = 1
    return char_dict

def gen_num_char_list(filepath):
    num_char_dict = get_num_chars(filepath)
    #print("num_char_dict: " + str(num_char_dict))
    data = [{"char":key, "num":value} for key,value in num_char_dict.items()]
    #print("data:" + str(data))
    data.sort(key=lambda d: d["num"],reverse=True)
    return data

def report(list_char_counts, filepath):
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + filepath + "...")
    print("----------- Word Count ----------")
    get_num_words(filepath=filepath)
    print("--------- Character Count -------")
    for entry in list_char_counts:
        if entry["char"].isalpha():
            print(str(entry["char"]) + ": "+ str(entry["num"]))
    print("============= END ===============")
    
