#include <cs50.h>
#include <stdio.h>

int main(void)

{
    int x=get_int ("x= ");
    int y=get_int ("y= ");
    int z=get_int ("z= ");

    if (x+z>y)
    {
        return 0;
    }
    else if (y+z>x)
    {
        return 0;
    }
    else if (x+y>z)
    {
        return 0;
    }
    else
    {
        printf("FALSE");
    }
}
