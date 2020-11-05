#include <stdio.h>
#include <cs50.h>

void get_positive_number(void);

int main(void)
{
    get_positive_number();

}

void get_positive_number(void)
{

    //prompting them for a positive integer between, say, 1 and 8, inclusive.
    int height;
    do


        height = get_int("Height:\n");

    while (height < 1 || height > 8);


    //# blocks building
    for (int i = 1; i <= height; i++)
    {


        for (int j = 1; j <= height - i; j++)
        {

            printf(" ");

        }
        for (int k = 1; k < i; k++)
        {
            printf("#");
        }

        printf("#\n");
    }

}