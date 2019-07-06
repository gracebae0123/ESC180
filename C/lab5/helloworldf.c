#include <stdio.h>
float bsqrt(float x,float accuracy);
float abs(float x);
int main(){
   for (int i =0; i<10, i++){
      float sqrt;
      sqrt = bsqrt((float)i,0.001);
      printf("The sqrt of %d is %f\n",i,sqrt);
   }
   return 0;
}

float abs(float x){
   if x>0{
      return x;
   }
   elif x<0{
      return -x;
   }
   else{
      return 0;
   }
}

float bsqrt(float x,float accuracy){
   float est = x/2;
   while (abs(x - est*est)>accuracy){    
      est = (est + x/est)/2;
   }
   return est;
}
