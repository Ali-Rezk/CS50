#include <cs50.h>
#include <stdio.h>

int main(void)

{
    int x=get_int ("x= ");
    int y=get_int ("y= ");
    int z=get_int ("z= ");

    if (x+z>y)
    {
        return 1;
    }
    else if (y+z>x)
    {
        return 1;
    }
    else if (x+y>z)
    {
        return 1;
    }
    else
    {
        printf("FALSE");
    }
}
