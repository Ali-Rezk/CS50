#include <cs50.h>
#include <stdio.h>

int main(void)

{
    int x=get_int ("x= ");
    int y=get_int ("y= ");
    int z=get_int ("z= ");

    if (x+z<y)
    {
        printf("FALSE\n");
    }
    else if (y+z<x)
    {
        printf("FALSE\n");
    }
    else if (x+y<z)
    {
        printf("FALSE\n");
    }
    else
    {
        printf("TRUE\n");
    }
}
