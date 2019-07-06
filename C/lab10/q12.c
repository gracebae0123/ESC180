int histogram (int *n, histo *m, int s) {
   int i;
   int j;
   int counter;
   m = (histo *)malloc(s*sizeof(histo));
   if (n == NULL || m == NULL) {
      return -1;
   }
   for (i=0;i<s;i++) {
      counter = 0;
      m[i].value = n[i];
      for (j=0;j<s;j++) {
         if (m[i].value == n[j]) {
             counter = counter + 1;
         }
      }
      m[i].frequency = counter;
    }
    return 0;
}
