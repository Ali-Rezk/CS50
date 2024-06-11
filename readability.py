def main():
    s = input("text: ")
    words = compute_spaces(s)
    letters = compute_alpha(s)
    sentences = compute_punct(s)
    L = letters / words * 100
    S = sentences / words * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    Z = round(index)

    if index < 1:
        print("Before Grade 1")

    elif Z > 16:
        print("Grade 16+")

    else:
        print(F"Grade {Z}")

    print()


def compute_alpha(letter):

    alpha = 0

    for i in range(len(letter)):
        if letter.isalpha():
            alpha += 1
    return alpha


def compute_spaces(words):

    spaces = 0

    for i in range(len(words)):
        if not words:
            spaces += 1

    return spaces + 1


def compute_punct(sentence):

    punct = 0

    for i in range(len(sentence)):
        if (sentence[i] == '!'):
            punct += 1

        elif (sentence[i] == '.'):
            punct += 1

        elif (sentence[i] == '?'):
            punct += 1

    return punct


main()
