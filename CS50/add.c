#include <stdio.h>
#include <cs50.h>

int main(void)

{
    int x=get_int("x is: ");
    int y=get_int("y is: ");
    int i=(x+y);
    printf("calls is:%i\n",i);
}
