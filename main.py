# PYTHON MODULE IMPORTs
import sys

# OWN MODULE IMPORTs
from stats import get_num_words
from stats import get_num_chars
from stats import sort_chars

#frankenstein_file_pth = "books/frankenstein.txt"

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
    #book_words_count = count_book_words(get_book_text("books/frankenstein.txt"))
    #print("Found %s total words" % book_words_count)

    # GET BOOK CHARs COUNT
    #char_count_list = get_book_chars_list(get_book_text("books/frankenstein.txt"))
    #print(char_count_list)
    
    # CHECK IF ARGUMENT WAS GIVEN
    if len(sys.argv) < 2:
        # USAGE EXPLANATION
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    file_pth = sys.argv[1]
        
    ## REPORT
    print("============ BOOKBOT ============")
    print("Analyzing book found at %s..." % file_pth)
    print("----------- Word Count ----------")
    print("Found %s total words" % get_num_words(get_book_text(file_pth)))
    print("--------- Character Count -------")
    # CREATE SORTED LIST OF CHARs
    chars_sorted_array = sort_chars(get_num_chars(get_book_text(file_pth)))
    for char_dict in chars_sorted_array:
        print("%s: %s" % (char_dict["name"], char_dict["num"]))
    print("============= END ===============")
            
# RUN PROGRAM
main()