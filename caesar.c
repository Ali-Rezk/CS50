#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int alph[]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,15,16,17,18,19,20,21,22,23,24,25};

int cipher(string l);

int main(int argc,string argv[])
{
    string s = get_string("plaintext:  ");
    int k = atoi(argv[1]);

    if (argc>2 || argc<2)
    {
        printf("Usage: ./caesar key");
    }
    else if (atoi(argv[1])<0)
    {
        printf("Usage: ./caesar key");
        return 1;
    }

    int p[] = cipher(s);

    for (int i=0, len=strlen(s); i<len; i++)
    {
        int c = (p[i] + k) %26;
        int z[i] = c
        printf("output: %c",z[i]+65);
    }
    printf("\n");
}

int cipher(string l)
{
    int score = 0;
    int p[];

    for (int i=0, len=strlen(l); i<len; i++)
    {
        if (isupper(l[i]))
        {
            score = alph[l[i]-'A'];
            p[i]  = score;
        }
        else if (islower(l[i]))
        {
            score += alph[l[i]-'a'];
            p[i]  = score;
        }
    }
    return p[];
}
