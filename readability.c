#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdio.h>

int compute_alpha(string letter);
int compute_spaces(string words);

int main (void)
{
    string s = get_string ("text: ");

    
}

int compute_alpha(string letter)
{
    int alpha = 0;

    for (int i=0, len=strlen(letter); i<len; i++)
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

    for (int i=0, len=strlen(words); i<len; i++)
    {
        if (isblank(words[i]))
        {
            spaces += 1;
        }
    }
    return spaces+1;
}

int compute_punct(string sentence)
{
    int punct = 0;

    for (int i=0, len=strlen(sentence); i<len; i++)
    {
        if (ispunct(sentence[i]))
        {
            punct += 1;
        }
    }
    return punct;
}
