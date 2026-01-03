# COUNT WORDs IN GIVEN BOOK
def get_num_words(text_data):
    book_words_list = text_data.split()
    return len(book_words_list)

def get_num_chars(text_data):
    # PREP VARs
    char_set = set()
    char_count_list = {}
    
    # TRANSFORM TEXT-DATA TO BE ALL LOWERCASE
    text_data = text_data.lower()
    
    # GET ALL CHARs INTO A SET WITHOUT DUPLICATEs!
    for char in text_data:
        char_set.add(char)
    
    # GET FOR EVERY CHAR IN THE SET THE COUNT HOW
    # OFTEN IT APPEARS IN THE BOOK
    for char in char_set:
        char_count_list[char] = text_data.count(char)
    
    return char_count_list

# DEFINITION OF RULE FOR SORT() 
def sort_on(items):
    return items["num"]

# SORT CHARs FROM HIGH -> LOW
def sort_chars(char_dict):
    
    # FIRST CREATE AN ARRAY WITH AN DICTIONARY PER CHAR
    char_array = []
    #print(char_dict)
    for char in char_dict:
        char_array.append({"name" : char, "num" : char_dict[char]})

    # SORT NOW WITH OUR DEFINED RULE THE CHAR LIST
    char_array.sort(reverse=True, key=sort_on)
    return char_array