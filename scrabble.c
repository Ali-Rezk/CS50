#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)

{
    string s = get_string ("player 1:");
    string z = get_string ("player 2:");
    char (A)= 1;
    for (int i=0, n = strlen(s); i<n; i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            s[i]-32;
        }
        printf("%i\n",s[i]);
    }

     for (int i=0, n = strlen(z); i<n; i++)
     {
        if (z[i] >= 'a' && z[i] <= 'z')
        {
            z[i]-32;
        }
    }


}
