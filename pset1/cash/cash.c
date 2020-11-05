#include <math.h>
#include <cs50.h>
#include <stdio.h>

void process(void);

int main(void)
{
    process();

}
//this function makes alot, wooh, that was hard, thats hardvard
void process(void)
{
    int quarter = 25;
    int dime = 10;
    int nickel = 5;
    int pennie = 1;
    int cents;
    int remain;
    int divider;
    int total_divider;


    //prompt the user for input as dollars in loop to control negative number
    float dollars;

    do
    {
        dollars = get_float("How much change is owed in dollars:");
        cents = round(dollars * 100);
    }
    while (dollars <= 0);
    divider = 0;
    remain = 0;
    total_divider = 0;

    for (int i = 0; i < cents; i++)
    {



        if (cents >= quarter)
        {
            remain = cents % quarter;
            //calculate division
            divider = cents / quarter;
            total_divider = total_divider + divider;

        }
        else if (cents >= dime)
        {
            remain = cents % dime;
            //calculate division
            divider = cents / dime;
            total_divider = total_divider + divider;

        }
        else if (cents >= nickel)
        {
            remain = cents % nickel;
            //calculate division
            divider = cents / nickel;
            total_divider = total_divider + divider;

        }
        else
        {
            remain = cents % pennie;
            //calculate division
            divider = cents / pennie;
            total_divider = total_divider + divider;

        }

        cents = remain;


    }//for-loop curly bracket
    printf("%i\n", total_divider + cents);

}
