#include <cs50.h>
#include <stdio.h>

int main (void)

{
    int n=get_int("change owned: ");
    while (n<0)
    {
        n=get_int("change owned: ");
    }

    float x=(n/25);
    float y=(n/10 - x*2.5);
    float z=(n/5 - x*5);
    float v=(n/1 - x*25);
    int i=(x+y+z+v);
    printf("%i\n",i);

}
