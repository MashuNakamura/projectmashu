/*
 * checkRetChars.c
 * calls three assembly language functions and
 * prints their return characters.
 *
 * 2017-09-29: Bob Plantz
 */

#include <stdio.h>
int A(void){
    return 'A';
}
int z(void){
    return 'z';
}
int hashtag(void){
    return 'h';
}

int main()
{
    char aCharacter;

    aCharacter = A();
    printf("Here some characters: %c, ", aCharacter);

    aCharacter = z();
    printf("%c, ", aCharacter);

    aCharacter = hashtag();
    printf("and %c.\n", aCharacter);

    return 0;
}
