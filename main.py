import sys

from stats import get_words, count_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents







def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]  
    file_contents = get_book_text(path_to_book)

    word_count = get_words(file_contents)
    sorted_list = count_characters(file_contents)

    
            
    print("============ BOOKBOT ============")
    print("Analyzing book found...")
    print("----------- Word Count ----------")
    print("Found" " " f"{word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()

if __name__ == "__main__":
    main()
