#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t byte;

int main(int argc, char *argv[])
{
    if (argc > 2)
    {
        return 1;
    }

    char *infile = argv[1];
    if (infile == NULL)
    {
        printf("Could not open file \n");
        return 1;
    }

    char outfile[8];
    int i = 0;
    FILE *src = fopen(infile, "r");
    FILE *img;
    byte buffer[512];
    int f = 0;
    while (fread(buffer, 512, 1, src) != 0)
    {

        if (buffer[0] == 0xff & buffer[1] == 0xd8 & buffer[2] == 0xff & (buffer[3] & 0xf0) == 0xe0)
        {
            sprintf(outfile, "%03i.jpg", i);
            if (f)
            {
                f = 0;
                fclose(img);
            }
            img = fopen(outfile, "w");
            f = 1;
            i++;
        }
        if (i)
        {
            fwrite(buffer, 512, 1, img);
        }
    }
    fclose(src);
    fclose(img);
}
