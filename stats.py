# COUNT WORDs IN GIVEN BOOK
def count_book_words(text_data):
    book_words_list = text_data.split()
    return len(book_words_list)

def get_book_chars_list(text_data):
    # PREP VARs
    char_set = set()
    char_count_list = {}
    
    # TRANSFORM TEXT-DATA TO BE ALL LOWERCASE
    text_data = text_data.lower()
    
    # GET ALL CHARs INTO A SET WITHOUT DUPLICATEs!
    for char in text_data:
        char_set.add(char)
    
    # GET FOR EVERY CHAR IN THE SET THE COUNT HOW OFTEN IT APPEARS IN THE BOOK
    for char in char_set:
        char_count_list[char] = text_data.count(char)
    
    return char_count_list