def sort_on(dict):
    return dict["letter"]


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

        print(f"--- Begin report of {book_path} ---")
        print(f"{len(words)} words found in the document\n")

        letters = []
        for key in letter_count:
            if key.isalpha():
                letters.append({"letter": key, "count": letter_count[key]})

        letters.sort(reverse=False, key=sort_on)

        for i in range(0, len(letters)):
            print(f"The '{letters[i]["letter"]}' character was found {
                  letters[i]["count"]} times")

        print("--- End Report ---")


main()
