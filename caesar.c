#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

alph[]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,15,16,17,18,19,20,21,22,23,24,25};

int main(int argc,string argv[])
{
    string s = get_string("plaintext:  ");

    if (argc>2 || argc<2)
    {
        printf{"Usage: ./caesar key"};
    }
    else if (isalpha(argv[1]))
    {
        printf{"Usage: ./caesar key"};
        return 1;
    }
    else if (atoi(argv[1]);<0)
    {
        printf{"Usage: ./caesar key"};
        return 1;
    }
}

int cipher(int k)
{
    int score = 0;

    for (int i=0, len=strlen(k); i<len; i++)
    {
        if (isupper(s[i]))
        {
            score 
        }
    }
}
