#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int b;
    int r;
    int g;
    for (int i = 0, len = width; i < len; i++)
    {
        image[i].rgbtBlue = b;
        image[i].rgbtRed = r;
        image[i].rgbtGreen = g;
        int x = b + r + g;
        int z = (int) round(x / 3);
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
