#include <stdio.h>
void printMatrix(int input[][4],int row, int column) ;
int main(){
   int array[3][4] = {{1,3,5,5},
                      {8,0,2,6},
                      {4,7,9,9}};
   printMatrix(array,3,4);
   return 0;
}


void printMatrix(int input[][4],int row, int column) {
   int horizontal;
   int vertical; 
   for (int horizontal = 0; horizontal < row; horizontal++){
      for (int vertical = 0; vertical < column; vertical++){
         printf("%8.3d",input[horizontal][vertical]);
      }
      printf("\n");
   }
}



