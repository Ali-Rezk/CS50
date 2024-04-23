#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int b;
    int r;
    int g;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            b = image[i][j].rgbtBlue;
            r = image[i][j].rgbtRed;
            g = image[i][j].rgbtGreen;
            int x = b + r + g;
            int z = (int) round(x / 3);
            image[i][j].rgbtBlue = z;
            image[i][j].rgbtRed = z;
            image[i][j].rgbtGreen = z;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int b;
    int r;
    int g;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            b = image[i][j].rgbtBlue;
            r = image[i][j].rgbtRed;
            g = image[i][j].rgbtGreen;
            int xb = 0.189 * b + 0.393 * r + 0.769 g;
            int xr = b + r + g;
            int xg = b + r + g;
            int z = (int) round(x / 3);
            image[i][j].rgbtBlue = z;
            image[i][j].rgbtRed = z;
            image[i][j].rgbtGreen = z;
        }
    }
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
