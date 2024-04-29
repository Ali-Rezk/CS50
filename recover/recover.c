#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t byte;

int main(int argc, char *argv[])
{
    char* infile = argv[1];
    FILE* src = fopen(infile, "r");
    char* dst = NULL;
    FILE* img;
    byte buffer[512];

    while (fread(buffer,512,1,src) != 0)
    {
        if (buffer[0] == 0xff & buffer[1] == 0xd8 & buffer[2] == 0xff & (buffer[3] & 0xf0) == 0xe0 )
        {
            sprintf(dst, "%03i.jpg", 2);
            img = fopen(dst, "w");
        }

        fwrite(buffer,512,1,img);
    }
    fclose(src);
    fclose(img);
}
