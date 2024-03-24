#include <cs50.h>
#include <stdio.h>

int main(void)

{
    int x=get_int ("x= ");
    int y=get_int ("y= ");
    int z=get_int ("z= ");

    if (x+z>y)
    {

    }
    else if (y+z>x)
    {
    printf("good");
    }
    else if (x+y>z)
    {
    return 1;
    }
    else if (z>y)
    {
        printf("TRUE");
    }
    else
    {
        printf("FALSE");
    }
}
