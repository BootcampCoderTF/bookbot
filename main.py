def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

        words = file_contents.split()
        word_count = len(words)
        print("")
        print(f"There are {word_count} words in ths text!")

main()