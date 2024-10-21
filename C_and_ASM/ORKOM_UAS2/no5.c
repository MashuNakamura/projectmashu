#include <stdio.h>
char fn1(void){
    return 'A';
}

char fn2(void){
    return 'B';
}

char fn3(void){
    return 'C';
}

int main(void){
    printf("%c ", fn1());
    printf("%c ", fn2());
    printf("%c ", fn3());
}
