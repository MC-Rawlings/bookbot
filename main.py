def sort_on(dict, key):
    return dict[key]


def sort_dict(dict):
    dict.sort(reverse=True, key=sort_on)


def main():
    book_path = './books/frankenstein.txt'
    with open(book_path) as f:
        file_contents = f.read()
        letter_count = {}

        for char in file_contents:
            lowered_char = char.lower()
            if lowered_char not in letter_count:
                letter_count[lowered_char] = 1
            else:
                letter_count[lowered_char] += 1

        words = file_contents.split()
        print(f"{file_contents}")
        print(f"{len(words)}")

        print(f"--- Begin report of {book_path} ---")
        print(f"{len(words)} words found in the document\n")

        for key in letter_count:
            print(f"The '{key}' character was found {letter_count[key]} times")


main()
