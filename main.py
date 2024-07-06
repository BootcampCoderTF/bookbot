def main():
    book_path = "books/frankenstein.txt"
    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"The file at {book_path} was not found.")
        return
    num_words = get_num_words(text)
    char_count = get_num_chars(text)
    
    print("=" * 80)
    print(f"\nText from {book_path}:\n{'=' * 80}\n")
    print(text)
    print("\n" + "=" * 80 + "\n")
    print(f"--- Begin Report of {book_path} --- \n")
    print(f"There are {num_words} words in this text!\n")
    
    for key in sorted(char_count):
        count = char_count[key]
        time_label = "time" if count == 1 else "times"
        print(f"The character '{key.upper()}' appears: {count} {time_label}")
    
    print("\n --- End Report --- \n")
    print("\n" + "=" * 80)

def get_num_words(text):
    """Returns the number of words in the text."""
    words = text.split()
    return len(words)

def get_book_text(path):
    """Reads text from a file and returns it."""
    with open(path) as f:
        return f.read()
    
def get_num_chars(text):
    """Returns the number of characters in the text, ignoring non-letter characters."""
    text = text.lower()
    chars = {}
    
    for c in text:
        if not c.isalpha():
            continue
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

main()