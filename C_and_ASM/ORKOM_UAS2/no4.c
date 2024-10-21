#include <stdio.h>

int fn1(void){
    return 10;
}

int fn2(void){
    return 20;
}

int fn3(void){
    return 30;
}

int main(void){
    printf("%d ", fn1());
    printf("%d ", fn2());
    printf("%d ", fn3()); 
}
