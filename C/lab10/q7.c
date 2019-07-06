#include <stdio.h>
int main(void){
   int *b;
   int **a;
   int c = 10;
   int d = 20;
   int q = 30;
   b = &c;
   a= &b;
   q = **a;
   *b = 0;
   d = c+100;
   q = q+100;
   printf("a = %d\n",**a);
   printf("b = %d\n",*b);
   printf("c = %d \n",c);
   printf("d = %d \n",d);
   printf("q = %d\n",q);
   return 0;
}
