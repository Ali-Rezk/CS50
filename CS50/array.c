#include<cs50.h>
#include<stdio.h>

int main(void)

{
    int array[5];

    for (int i=0; i<5; i++)
    {
        array[i] =get_int("insert number: ");
    }

    printf("%i,%i,%i,%i,%i\n",array[0],array[1],array[2],array[3],array[4]);
}
