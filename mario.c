#include <cs50.h>
#include <stdio.h>

void print_rows(int length);

void print_bricks(int bricks);

int main(void)

{
    int n = get_int("height:");
    for (int i = 0; i < n; i++)
    {
        print_bricks(n - i - 1);
        print_rows(i + 1);
        printf(" ");
        print_rows(i + 1);
        printf("\n");
    }
}
void print_rows(int length)
{
    for (int i = 0; i < length; i++)
    {
        printf("#");
    }
}
void print_bricks(int bricks)
{
    for (int i = 0; i < bricks; i++)
    {
        printf(" ");
    }
}
