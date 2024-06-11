


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

    elif (Z > 16)
        print("Grade 16+")

    else
        print("Grade %i", Z)

    print()


def compute_alpha(letter)
{
    alpha = 0

    for (int i = 0, len = strlen(letter); i < len; i++)
    {
        if (isalpha(letter[i]))
        {
            alpha += 1
        }
    }
    return alpha
