#include <cs50.h>
#include <stdio.h>

int main (void)

{
    int n=get_int("change owned: ");
    while (n<0)
    {
        n=get_int("change owned: ");
    }

    int x=(n/25);
    int y=(n/10 - x*2.5);
    int z=(n/5 - x*5);
    int v=(n/1 - x*25);
    int i=(x+y+z+v);
    printf("%i\n",i);

}
