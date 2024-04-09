#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int alph[]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,15,16,17,18,19,20,21,22,23,24,25};

int main(int argc,string argv[])
{
    string s = get_string("plaintext:");
    int k = atoi(argv[1]);

    if (argc != 2)
    {
        printf("Usage: ./caesar key");
        return 1;
    }
    else if (atoi(argv[1])<0)
    {
        printf("Usage: ./caesar key");
        return 1;
    }

    printf("output:   ");
    int x = strlen(s);
    int upp[x];
    int c[x];
    int low[x];
    int v[x];
    memset(upp,0,sizeof(x));
    memset(low,0,sizeof(x));
    memset(v,0,sizeof(x));
    memset(c,0,sizeof(x));
    for (int i=0, len=strlen(s); i<len; i++)
    {
        if (isupper(s[i]))
        {
            int score = alph[s[i]-'A'];
            upp[i] = score;
            c [i] = (upp[i] + k) %26;
            printf("%c",c[i]+65);
        }
        else if (islower(s[i]))
        {
            int score = alph[s[i]-'a'];
            low[i] = score;
            v [i] = (low[i] + k) %26;
            printf("%c",v[i]+97);
        }
    }
    printf("\n");
}

