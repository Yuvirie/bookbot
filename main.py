from stats import count_words, count_chars, report
import sys

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main():

    #check the args

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = sys.argv[1]

    contents = get_book_text(book)

    num_words = count_words(contents)

    print(f"{num_words} words found in the document")

    num_chars = count_chars(contents)

    print(num_chars)

    report_data = report(num_chars)

    print(f"""============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    
    for item in report_data:
        print(f"{item["char"]}: {item["count"]}")

    print("============= END ===============")



main()