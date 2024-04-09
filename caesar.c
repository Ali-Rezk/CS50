#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int alph[]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,15,16,17,18,19,20,21,22,23,24,25};

int main(int argc,string argv[])
{
    string s = get_string("plaintext:  ");
    int k = atoi(argv[1]);

    if (argc != 2)
    {
        printf("Usage: ./caesar key");
    }
    else if (atoi(argv[1])<0)
    {
        printf("Usage: ./caesar key");
        return 1;
    }

    int score = 0;

    for (int i=0, len=strlen(s); i<len; i++)
    {
        if (isupper(s[i]))
        {
            score = alph[s[i]-'A'];
            int upp[i] = score;
            int c [i] = (upp[i] + k) %26;
            printf("output: %c",c[i]+65);
        }
        else if (islower(s[i]))
        {
            score = alph[s[i]-'a'];
            int low[i]  = score;
            int v [i] = (low[i] + k) %26;
            printf("output: %c",v[i]+97);
        }
    }

    for (int i=0, len=strlen(s); i<len; i++)
    {
        int c [i]= (upp[i] + k) %26;
        printf("output: %c",c[i]+65);
    }
    printf("\n");
}

int cipher(string l,int v[])
{
    int score = 0;

    for (int i=0, len=strlen(l); i<len; i++)
    {
        if (isupper(l[i]))
        {
            score = alph[l[i]-'A'];
            int v[i]  = score;
        }
        else if (islower(l[i]))
        {
            score = alph[l[i]-'a'];
            int v[i]  = score;
        }
    }
    return v[];
}
