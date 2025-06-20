from stats import count_words, count_characters, chars_to_sorted_list
import sys


def get_book_text(filepath):
    
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    
    # print(get_book_text(path))
    
    txt = get_book_text(path)
    # print(count_words(txt))
    # print(count_characters(txt))

    sorted_chars = chars_to_sorted_list(count_characters(txt))
    
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(count_words(txt))
    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        value = item["value"]
        print(f"{char}: {value}")
    
    print("============= END ===============")
       
main()

