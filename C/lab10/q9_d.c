int fil(float *matrixIn, int rows, int cols, float ** matrixOut){
   int r = 0;
   int c =0;
   if (matrixIn == NULL){
      return -1;
   }
   *matrixOut = (float *)malloc(sizeof(int)*rows*cols);
   if (*matrixOut == NULL){
      return -1;
   }
   for (r=0;r<rows;r++){
      for(c=0;c<cols;c++){
         if (matrixIn[r*c+c] < 0){
            matrixOut[r*c+c] = 0;
         } 
         else{
            matrixOut[r*c+c] = matrixOut[r*c+c];
         }
      }
   }
   return 0;
}
         
