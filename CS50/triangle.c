#include <cs50.h>
#include <stdio.h>

int main(void)

{
    float x=get_float ("x= ");
    float y=get_float ("y= ");
    float z=get_float ("z= ");

    if (x<=0 || y<=0 || z<=0)
    {
        printf("FALSE\n");
    }
    else if (x+z<=y)
    {
        printf("FALSE\n");
    }
    else if (y+z<=x)
    {
        printf("FALSE\n");
    }
    else if (x+y<=z)
    {
        printf("FALSE\n");
    }
    else
    {
        printf("TRUE\n");
    }
}
