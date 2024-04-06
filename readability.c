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
    int alpha=0;

    for (int i=0, len=strlen(s); i<len; i++)
    {
        if (isalpha(s[i]))
        {
            alpha += 1;
        }
    }
}
