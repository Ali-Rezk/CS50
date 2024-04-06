#include <cs50.h>
#include <stdio.h>
#include <string.h>

int points=[1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10];

int main(void)

{
    string s = get_string ("player 1:");
    string z = get_string ("player 2:");
    int ('A')= 1;
    for (int i=0, n = strlen(s); i<n; i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            s[i]=s[i]-32;
        }
        printf("%i\n",s[i]);
    }

     for (int i=0, n = strlen(z); i<n; i++)
     {
        if (z[i] >= 'a' && z[i] <= 'z')
        {
            z[i]=z[i]-32;
        }
    }

}
