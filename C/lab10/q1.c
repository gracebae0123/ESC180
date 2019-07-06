#include <stdio.h>
//float average (float *input, int size);
//int main(){
//   float input[5] = {1,3,5,7,3};
//   float rval;
//   rval = average (input, 5);
//   printf("average : %f",rval); 
//   return 0;
//}
float average (float *input, int size){
   float average =0;
   float sum = 0;
   int i = 0;
   for (i =0; i<size; i++){
      sum = sum + input[i];
   }
   average = sum/size;
   return average;
}


      
