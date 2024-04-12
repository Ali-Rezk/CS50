#include <cs50.h>
#include <stdio.h>

int main(void)
{

int n = get_int("n = ");
int z = 0;
while (n > 1)
{
    n = n/2;
    z += 1;
}
printf("%i\n",z);
}
