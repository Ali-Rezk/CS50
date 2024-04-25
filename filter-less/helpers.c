#include "helpers.h"
#include <math.h>

int b;
int r;
int g;

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            b = image[i][j].rgbtBlue;
            r = image[i][j].rgbtRed;
            g = image[i][j].rgbtGreen;

            int x = b + r + g;
            int z = (int) round(x / 3.0);

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
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            b = image[i][j].rgbtBlue;
            r = image[i][j].rgbtRed;
            g = image[i][j].rgbtGreen;

            int xb = (int) round(0.131 * b + 0.272 * r + 0.534 * g);
            int xr = (int) round(0.189 * b + 0.393 * r + 0.769 * g);
            int xg = (int) round(0.168 * b + 0.349 * r + 0.686 * g);

            if (xb > 255)
            {
                xb = 255;
            }
            if (xr > 255)
            {
                xr = 255;
            }
            if (xg > 255)
            {
                xg = 255;
            }

            image[i][j].rgbtBlue = xb;
            image[i][j].rgbtRed = xr;
            image[i][j].rgbtGreen = xg;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE reflect[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            reflect[i][j] = image[i][width - j - 1];
        }
        for (int k = 0; k < width; k++)
        {
            image[i][k] = reflect[i][k];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE blur[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            r = 0;
            g = 0;
            b = 0;
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    if (0 <= i + k && i + k < height && 0 <= j + l && j + l < width)
                    {
                        r += image[i + k][j + l].rgbtRed;
                        g += image[i + k][j + l].rgbtGreen;
                        b += image[i + k][j + l].rgbtBlue;
                    }
                }
            }
            if (i == 0 || i == height - 1 & j == 0 || j == width - 1)
            {
                blur[i][j].rgbtRed = (int) round (r / 4.0);
                blur[i][j].rgbtGreen = (int) round (g / 4.0);
                blur[i][j].rgbtBlue = (int) round (b / 4.0);
            }
            else if (i == 0 || i == height - 1 || j == 0 || j == width - 1)
            {
                blur[i][j].rgbtRed = (int) round (r / 6.0);
                blur[i][j].rgbtGreen = (int) round (g / 6.0);
                blur[i][j].rgbtBlue = (int) round (b / 6.0);
            }
            else
            {
                blur[i][j].rgbtRed = (int) round (r / 9.0);
                blur[i][j].rgbtGreen = (int) round (g / 9.0);
                blur[i][j].rgbtBlue = (int) round (b / 9.0);
            }
        }
    }
    for (int z = 0; z < height; z++)
    {
        for (int y = 0; y < width; y++)
        {
            image[z][y] = blur[z][y];
        }
    }
    return;
}
