#include <stdio.h>
int analboard(char *T,int sizeT);
int main(){
   {
   char T[9] = {'-','X','O',
               'O','X','-',
               'O','X','-'};
   printf("%s\n",analboard(T,9)=='X'?"GOOD":"BAD");
   }
   {
   char T[9] = {'-','X','O',
               'X','O','-',
               'O','X','-'};
   printf("%s\n",analboard(T,9)=='O'?"GOOD":"BAD");
   }
   {
   char T[9] = {'X','X','X',
               'O','O','0',
               'O','X','0'};
   printf("%s\n",analboard(T,9)=='X'?"GOOD":"BAD");
   }
   {
   char T[9] = {'0','0','0',
               'O','O','0',
               'O','X','0'};
   printf("%s\n",analboard(T,9)=='0'?"GOOD":"BAD");
   }
   return 0;
}

int analboard(char *t,int sizeT){
   int colSize=sizeT/3;
   int row1=0;
   int row2=colSize*1;
   int row3=colSize*2;
   
   if (t[row1+0] == t[row1+1]&& t[row1+1] == t[row1+2]&& t[row1] != '-'){
      return t[row1+0];
   }
   printf("LINE: %d\n",__LINE__);
   if (t[row2+0] == t[row2+1]&& t[row2+1] == t[row2+2]&&t[row2] != '-'){
      return t[row2+0];
   }
   printf("LINE: %d\n",__LINE__);
   if (t[row3+0] == t[row3+1]&& t[row3+1] == t[row3+2]&&t[row3] != '-'){
      return t[row3+0];
   }
   printf("LINE: %d\n",__LINE__);
  
   int col1=0;
   int col2=1;
   int col3=2;
   
   if (t[col1] == t[col1+3] && t[col1+3]== t[col1+6]&&t[col1] != '-'){
      return t[col1];
   }
   printf("LINE: %d\n",__LINE__);
   if (t[col2] == t[col2+3] && t[col2+3]== t[col2+6]&&t[col2] != '-'){
      return t[col2];
   }
   printf("LINE: %d\n",__LINE__);
   if (t[col3] == t[col3+3] && t[col3+3]== t[col3+6]&&t[col3] != '-'){
      return t[col3];
   }
   printf("LINE: %d\n",__LINE__);

   int topleft = 0;
   if (t[topleft] == t[topleft+4] && t[topleft+4]== t[topleft+8]&&t[topleft] != '-'){
      return t[topleft];
   }
   printf("LINE: %d\n",__LINE__);
   int topright =2;
   if (t[topright] == t[topright+2]&& t[topright+2] == t[topright+4]&&t[topright] != '-'){
      return t[topright];
   }
   return 0;
}

    
