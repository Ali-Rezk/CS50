#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)

{
    string s = get_string ("player 1:");
    string z = get_string ("player 2:");

    for (int i=0, n = strlen(s); i<n; i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            printf("%c",s[i]-32);
        }
        else if (z[i] >= 'a' && z[i] =< 'z')
        {
            printf("%c",z[i]-32);
        
        }
    }
    printf("\n");
}
