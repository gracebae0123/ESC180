#include<stdio.h>
#include<stdlib.h>
typedef struct{ 
   float coefficient;
   int exp;
}poly;

poly* monkey(poly *input){
   input->exp = input->exp +1;
   input->coefficient = input->coefficient / input->exp;
   return input;
}

int chicken (poly input, poly *output){
   if(output == NULL){
      return -1;
   }
   output ->exp = input.exp +1;
   output -> coefficient = input.coefficient / output->exp;
   return 0;
}

int chicken2 (poly input, poly**output){
   if (output == NULL){
      return -1;
   }
   *output = (poly *)malloc(sizeof(poly));
   (*output)->exp = input.exp +1;
   (*output)->coefficient = input.coefficient/(*output)->exp;
   return 0;
}

int main(){
   poly p1;
   poly *mon;
   poly chi;
   poly *pinte;
   int rval;
   p1.coefficient = 4;
   p1.exp = 2;
   printf("<ORIGINAL> \n coefficient: %f, exp: %d\n",p1.coefficient, p1.exp);

   mon = monkey(&p1);
   printf("<INTEGRATE> \n coefficient: %f, exp: %d\n",mon->coefficient, mon->exp);

   p1.coefficient = 4;
   p1.exp = 2;

   rval = chicken(p1,&chi);
   printf("<INTEGRATE> \n coefficient: %f, exp: %d\n",chi.coefficient, chi.exp);

   rval = chicken2(p1, &pinte);
   printf("<INTEGRATE> \n coefficient: %f, exp: %d\n",pinte->coefficient, pinte->exp);

   return 0;
}
