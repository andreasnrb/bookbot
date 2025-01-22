def getCharCount(text):
    copy = text.lower()

    counted = {}
    for char in copy:
        if char in counted:
            counted[char] += 1
        else:
            counted[char] = 1
    return counted


def sort_on(tmp):
    return tmp["total"]


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = len(file_contents.split())
        chars = getCharCount(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")

        print("")
        tuples = []
        for char, total in chars.items():
            if char.isalpha():
                tuples.append({"char": char, "total": total})

        tuples.sort(reverse=True, key=sort_on)

        for x in tuples:
            char = x["char"]
            total = x["total"]
            print(f"The '{char}' character was found {total} times")
        print("")
        print("--- End report ---")


main()
