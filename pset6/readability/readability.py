from cs50 import get_string
import string

text = get_string("Text:")
print(f"Before {text}")
letters = 0
words = 0
sentences = 0
l = 0.0
s = 0.0
index = 0.0
n = len(text)
# Loop to calculate words,letters and sentences
for i in range(n):
    if (text[i].isalpha()):
        letters += 1
    if (text[i].isspace()):
        words += 1
    if (text[i] == '.' or text[i] == '?' or text[i] == '!'):
        sentences += 1
#         // printf("%c",tolower(ltext[i]));

words = words + 1
#     // printf("words: %i\n",words);
#     // printf("letters: %i\n",letters);
#     // printf("sentences: %i\n",sentences);
#     // printf("\n");
l = (letters / words) * 100
s = (sentences / words) * 100
index = round(0.0588 * l - 0.296 * s - 15.8)
#     // printf("l: %f\n",l);
#     // printf("s: %f\n",s);
#     // printf("index: %.i\n",index);
if (index <= 1):
    print("Before Grade 1")
elif (index > 16):
    print("Grade 16+")
else:
    print(f"Grade {index}")
touch