#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int compute_alpha(string letter);
int compute_spaces(string words);
int compute_punct(string sentence);

int main(void)
{
    string s = get_string("text: ");

    float words = compute_spaces(s);
    int letters = compute_alpha(s);
    int sentences = compute_punct(s);
    float L = letters / words * 100;
    float S = sentences / words * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int Z = (float) round(index);

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
}

int compute_alpha(string letter)
{
    int alpha = 0;

    for (int i = 0, len = strlen(letter); i < len; i++)
    {
        if (isalpha(letter[i]))
        {
            alpha += 1;
        }
    }
    return alpha;
}

int compute_spaces(string words)
{
    int spaces = 0;

    for (int i = 0, len = strlen(words); i < len; i++)
    {
        if (isblank(words[i]))
        {
            spaces += 1;
        }
    }
    return spaces + 1;
}

int compute_punct(string sentence)
{
    int punct = 0;

    for (int i = 0, len = strlen(sentence); i < len; i++)
    {
        if (sentence[i] == '!')
        {
            punct += 1;
        }
        else if (sentence[i] == '.')
        {
            punct += 1;
        }
        else if (sentence[i] == '?')
        {
            punct += 1;
        }
    }
    return punct;
}
