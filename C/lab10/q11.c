#include <stdio.h>
#include <stdlib.h>

int isPrime(int n){
   int i =1;
   int primeCnt = 0;
   for(i = 1; i <n; i++){
      if ( n%i == 0){
         primeCnt++;
      }
   }
   if(primeCnt == 1){
      return 0;
   }
   else{
      return -1;
   }
}

int isPrimeProduct(int n){
   int i = 1;
   int prmCnt = 0;
   int isprm = 10;
   for(i = 1; i<n; i++){

      isprm = isPrime(i);
      if(isprm == 0){ 
         isprm = isPrime(n/i);
         if(isprm == 0){
            return 0;
         }
         else{}
      }
      isprm = 10;
   }
   return -1;
}

/*
int main(){
   printf("isPrime(5) = %d\n", isPrime(5));
   printf("isPrime(7) = %d\n", isPrime(7));
   printf("isPrime(11) = %d\n", isPrime(11));
   printf("isPrimeProduct(15) = %d\n", isPrimeProduct(15));
   printf("isPrimeProduct(21) = %d\n", isPrimeProduct(21));
   return 0;
}
*/
      











