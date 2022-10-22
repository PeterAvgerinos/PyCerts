#include <stdio.h>

int i = 0;
char array[3] = "abc";
char temp;
while (i <= sizeof(array)){ 
    temp = array[i];
    ++i;
}

