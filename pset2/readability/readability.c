#include <stdio.h>
#include <cs50.h>
#include <ctype.h>  // for uppercase function
#include <string.h> // for lenght calculation strlen
#include <math.h>   ///to round up

void text_lowcase(string ltext);

int main(void)
{
    string text;
    text = get_string("Text:");
    // printf("Before %s\n",text);
    text_lowcase(text);


}
// lowercase and leght function
void text_lowcase(string ltext)
{
    int n;
    int letters             = 0;
    int words               = 0;
    int sentences           = 0;
    float l                 = 0.0;
    float s                 = 0.0;
    int index                 = 0.0;
    n = strlen(ltext);
    //Loop to calculate words,letters and sentences
    for (int i = 0; i < n; i++)
    {
        if (isalpha(ltext[i]) || ispunct(ltext[i] != true))
        {
            letters++;
        }
        if (isspace(ltext[i]))
        {
            words++;
        }
        if (ltext[i] == '.' || ltext[i] == '?' || ltext[i] == '!')
        {
            sentences++;
        }
        // printf("%c",tolower(ltext[i]));
    }
    words = words + 1;
    // printf("words: %i\n",words);
    // printf("letters: %i\n",letters);
    // printf("sentences: %i\n",sentences);
    // printf("\n");
    l = (letters / (float) words) * 100;
    s = (sentences / (float) words) * 100;
    index = round(0.0588 * l - 0.296 * s - 15.8);
    // printf("l: %f\n",l);
    // printf("s: %f\n",s);
    // printf("index: %.i\n",index);
    if (index <= 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}
