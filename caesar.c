#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



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
    }
    else if (atoi(argv[1]);<0)
    {
        printf{"Usage: ./caesar key"};
    }
}

