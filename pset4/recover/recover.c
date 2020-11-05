#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#define BLOCKSIZE 512

//prototypes
int inputError();
bool isJpgHeader(uint8_t buffer[]);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        return inputError();
    }
    char *inputFile = argv[1];
    if (inputFile == NULL)
    {
        return inputError();
    }
    FILE *inputPtr = fopen(inputFile, "r");
    if (inputPtr == NULL)
    {
        printf("unable to read file %s\n", inputFile);
        return 1;
    }
    //variables to start
    char file_name[8];
    FILE *outputPtr = NULL;
    uint8_t buffer[BLOCKSIZE];
    int jpgcounter = 0;

    while (fread(buffer, sizeof(uint8_t), BLOCKSIZE, inputPtr) || feof(inputPtr) == 0)
    {
        if (isJpgHeader(buffer))
        {
            if (outputPtr != NULL)
            {
                fclose(outputPtr);
            }
            //if it finds jpg-header
            sprintf(file_name, "%03i.jpg", jpgcounter);
            outputPtr = fopen(file_name, "w");
            jpgcounter++;
        }
        if (outputPtr != NULL)
        {
            fwrite(buffer, sizeof(buffer), 1, outputPtr);

        }
    }//while loop curly
    //close everything
    if (inputPtr == NULL)
    {
        fclose(inputPtr);
    }
    if (outputPtr == NULL)
    {
        fclose(outputPtr);
    }


}//main curly close

//INPUT Error function
int inputError()
{
    printf("Usage: ./recover image\n");
    return 1;
}
// this is checking conditions for beginning elements
bool isJpgHeader(uint8_t buffer[])
{
    return  buffer[0] == 0xff
            && buffer[1] == 0xd8
            && buffer[2] == 0xff
            && (buffer[3] & 0xf0) == 0xe0;
}