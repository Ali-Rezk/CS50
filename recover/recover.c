#include <stdio.h>
#include <stdlib.h>

typedef uint8_t byte;

int main(int argc, char *argv[])
{
    char* infile = argv[1];
    FILE* src = fopen(infile,"r");
    FILE* dst;
    byte buffer[512];

    while (fread(buffer,512,1,src) != 0)
    {
        if ()
        {
            fwrite(buffer,512,1,dst)
        }
    }
}
