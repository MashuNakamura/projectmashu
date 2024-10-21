#include <unistd.h>

char* rokokCik(void){
    return "Halo";
}

int main(void){
    write(1, rokokCik(), 4);
    return 0;
}
