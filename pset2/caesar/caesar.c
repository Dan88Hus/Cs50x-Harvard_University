#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

void container(int k);
// this main function is used for to find correct key
int main(int argc, string argv[])
{
    int count                   = 0;
    const int arg_count         = argc;
    const string argument       = argv[1];
    int key                       = 0;

    if (argc == 2)
    {
        int len_argv = strlen(argument);
        for (int i = 0; i < len_argv; i++)
        {
            if isdigit(argument[i])
            {

                count++;
                // printf("this works %c\n", argument[i]);

            }
            else
            {
                printf("Usage: %s key", argv[0]);
                return 1;

            }

        }// for curly
        if (count == len_argv)
        {
            // printf("Success\n");
            key = atoi(argument);
            // printf("key: %i\n", key);
            container(key);

        }
    }
    else if (argc == 0 || argc == 1 || argc >= 3 || (atoi(argv[1])) < 0)
    {
        printf("Usage: %s key", argv[0]);
        return 1;
    }

}// main curly
// this container function is used to find crypted words
void container(int k)
{
    string plaintext;


    plaintext = get_string("plaintext:");
    // printf("plaintext:%s\n", plaintext);
    // printf("key:%i\n",k);
    int p_length = strlen(plaintext);
    int c;
    char text;
    int cip[p_length];
    printf("ciphertext:");

    for (int i = 0; i < p_length; i++)
    {
        text = plaintext[i];
        if (isalpha(text))
        {
            if (isupper(text))
            {
                char p = text - 65;
                c = (p + k) % 26;
                cip[i] = c + 65;
                printf("%c", cip[i]);
            }
            if (islower(text))
            {
                char p = text - 97;
                c = (p + k) % 26;
                cip[i] = c + 97;
                printf("%c", cip[i]);
            }
        }
        else
        {
            cip[i] = text;
            printf("%c", cip[i]);
        }
    }//for loop curly
    printf("\n");
}//container-main curly