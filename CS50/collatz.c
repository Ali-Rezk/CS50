#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{

float n = get_int("n = ");
int z = 0;

while (n > 1)
{
int x = (int) round(n/2);
float y = n/2;

    if (y == x)
    {
        n = n/2;
        z += 1;
    }
    else if (y != x)
    {
        n = 3*n + 1;
        z += 1;
    }
}
printf("%i\n",z);
}
