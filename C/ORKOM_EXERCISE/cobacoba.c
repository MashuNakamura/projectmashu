/* checkRetNos.c
 * calls three assembly language functions and
 * prints their return numbers.
 *
 * 2017-09-29: Bob Plantz
 */

#include <stdio.h>
int positiveNumber(void){
    return 200;
}
int negativeNumber(void){
    return -20;
}
int maxNumber(void){
    return 999;
}

int main()
{
  int x;

  x = positiveNumber();
  printf("Here is a positive constant: %i, ", x);

  x = negativeNumber();
  printf("a negative constant: %i, ", x);

  x = maxNumber();
  printf("and the maximum number: %i.\n", x);

  return 0;
}
