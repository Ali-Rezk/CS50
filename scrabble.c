#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int points[] ={1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};
int compute_score(string word);

int main(void)

{
    string ask1= get_string ("player 1: ");
    string ask2= get_string ("player 2: ");

    int score1 = compute_score (ask1);
    int score2 = compute_score (ask2);

    if (score1>score2)
    {
        printf("player 1 wins");
    }
    else if (score2>score1)
    {
        printf("Player 2 wins");
    }
    else
    {
        printf("tie");
    }

    printf("\n");
}
int compute_score(string word)
{
    int score = 0;

    for (int i=0, n=strlen (word); i < n; i++)
    {
        if (isupper(word[i]))
        {
            score += points[word[i]-'A'];
        }
        else if (islower(word[i]))
        {
            score += points[word[i]-'a'];
        }

    }
    return score;
}
