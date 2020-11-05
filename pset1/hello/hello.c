#include <stdio.h>
#include <cs50.h>


int main(void)
{
    //this is going to prompt user name and get answer
    //as "name" variable to say hello,name
    string name = get_string("What is your name\n");
    printf("Hello, %s\n", name);


}

