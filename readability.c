#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdio.h>

int compute_alpha(string letter);

int main (void)
{

}

int compute_alpha(string letter)
{
    string s = get_string ("text: ");
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

    for (int i=0, len=strlen(sentence); i<len; i++)
    {
        if (isblank(sentence[i]))
        {
            spaces += 1;
        }
    }
    return spaces+1;
}

int compute_
