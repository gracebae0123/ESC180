#include <stdio.h>
int swap(int *a, int *b);
int main(){
   int a = 5;
   int b = 6;
   printf("BEFORE: a = %d, b = %d\n",a,b);
   swap(&a,&b);
   printf("AFTER: a = %d, b = %d",a,b);
   return 0;
}   

int swap(int *a, int *b){
   int temp = *a;
   *a = *b;
   *b= temp;
   return 1;
}


   
