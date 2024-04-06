#include <cs50.h>
#include <stdio.h>
#include <string.h>

int points=[1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10];
int compute_score(compute);

int main(void)

{
    string ask1= get_string ("player 1: ");
    string ask2= get_string ("player 2: ");

}
int compute_score(word)
{
    int score = 0;

    for (int i=0, n=strlen (word); i < n; i++)
    {
        if (isupper(s[i]))
        {
            score += points[word[i]-'A'];
        }
        else if (islower(s[i]))

    }
}
