from stats import count_book_words
from stats import get_book_chars_list

# OPEN AND RETURN FILE CONTENT
def get_book_text(file_pth):
    book_content = ""
    
    with open(file_pth) as data:
        book_content = data.read()

    return book_content
    
    
def main():
    # GET BOOK TEXT
    #print(get_book_text("./books/frankenstein.txt"))
    
    # GET BOOK WORDs COUNT
    book_words_count = count_book_words(get_book_text("./books/frankenstein.txt"))
    print("Found %s total words" % book_words_count)

    # GET BOOK CHARs COUNT
    char_count_list = get_book_chars_list(get_book_text("./books/frankenstein.txt"))
    print(char_count_list)
    
# RUN PROGRAM
main()