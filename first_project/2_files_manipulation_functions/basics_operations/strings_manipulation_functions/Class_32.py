#encoding message with python


def zenit_polar_replace(text):
    # doing encoding zenit polar using the method replace
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def main():
    # phrase entrance and encoding
    phrase = "The quick brown fox jumps over the lazy dog"
    phrase = phrase.title()  # uppercase to first letter of each word

    # split the phrase in each word
    words = phrase.split()

    # processing each word in list using zenit_polar
    coded_words = [zenit_polar_replace(word) for word in words]

    # join all encoding words in one prhase
    coded_phrase = " ".join(coded_words)
    print("Original:", phrase)
    print("Coded:", coded_phrase)


if __name__ == "__main__":
    main()