


def main():
    s = input("text: ")
    words = compute_spaces(s)
    letters = compute_alpha(s)
    sentences = compute_punct(s)
    L = letters / words * 100
    S = sentences / words * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    Z = round(index)

    if (index < 1)
    {
        printf("Before Grade 1");
    }
    else if (Z > 16)
    {
        printf("Grade 16+");
    }
    else
    {
        printf("Grade %i", Z);
    }

    printf("\n");
