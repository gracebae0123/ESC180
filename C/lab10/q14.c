#include <stdio.h>
#include <stdlib.h>

int fibo(int n){
   if(n<0){
      return -1;
   }
   
   if(n == 0 || n==1){
      return 1;
   }
   else if(n ==2){
      return 1;
   }
   else{ 
      return fibo(n-1) + fibo(n-2) + fibo(n-3);
   }

   return 0;
}
   

/* -test code-
int main(){
   printf("fibo(5) = %d\n", fibo(5));
   printf("fibo(4) = %d\n", fibo(4));
   printf("fibo(3) = %d\n", fibo(3));
   printf("fibo(2) = %d\n", fibo(2));
   
   return 0;
}
*/
   
   
