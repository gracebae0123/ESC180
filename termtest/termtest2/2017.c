1. ii, iv

2. 24

3. 5*3*2 = 30

4. n+1

5. 10+1

6. *Q = (struct vector *) malloc(10*sizeof(struct vector))

7. d= 3000 q= 2000 c= 0

8. Enable dynamic data structures

9. Bridge = linked list force = structs or arrays loop = while

10. Structs = variable type

11. (Diagram)

12 a.
   struct polynomial{
      int power;
      float coefficent;
   }
12 b. 
int monkey(struct* polynomial){
   polynomial->power = polynomial->power - 1;
   polynomial->coefficient = (polynomial->coefficient) / (polynomial->power);
   return 1;
}
   
   
12 c.
int chicken (struct *polynomial, struct *output){


d.
e. 


13 a. typeA = float *
      typeB = int  
      typeC = int  

13 b. typeD = float *
13 c. typeD = float **
13 d. 
int transpose(float * matrixIn, int rows, int cols, float ** matrixOut){
   int i;
   int j;
   if (matrixIn == NULL){
      return -1;
   }
   else if (*matrixOut == NULL){
      return -1;
   }
   if (matrixOut == NULL){
      *matrixOut = (float *)malloc(sizeof(float)*rows*cols);
   }
   for (i=0;i<rows;i++){
      for (j=0; j<cols;j++){
         matrixOut[



}
}}



14 a. typeA = float* A = input array
      typeB = int B = size of array

14 b. 
int bubbleSort (float *input, int size){
   int swapped;
   int i;
   float temp;
   swapped = 0;
   while (swapped == 1){
      for (i =1; i<size;i++){
         if (input[i-1] < input[i]){ 
            temp = 
   
   
   
   
