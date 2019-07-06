#include <stdio.h>
int bubblesort(int *array, int size);
int main(){
   int size = 5;
   int array[5] = {1,4,5,3,2};
   int i=0;
   printf("=====original=====\n");
   for (i=0; i <size;i++){
      printf("%d\n",array[i]);
   }    
   bubblesort(array, size);
   printf("=====new====\n");
   for (i = 0; i < size; i++){
      printf ("%d\n",array[i]);
   }
   return 0;
}




int bubblesort(int *array, int size){
   int i =0;
   int temp = 0;
   int j;
   for (i =0; i<size; i++){
      for (j=i+1;j<size;j++){
         if (array[i] > array[j]){
            temp = array[i];
            array[i] = array[j];
            array[j] = temp;
         }
      }
   }      

   if (swapped == 0){
      return 0;
   }
   else{
      return 1;
   }
}
      
      
   
