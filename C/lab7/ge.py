def ge_fw(matrix):
   row = 3
   column = 4
   #step 1: check first col != 0
   for i in range(0,row,1):
      if matrix[i][0] != 0:
         firstRow_nonZero = i
         printMatrix(matrix)
         break
         

   #step 2: swtich rows
   temp = matrix[0] 
   matrix[0] = matrix[firstRow_nonZero]
   matrix[firstRow_nonZero] = temp
   printMatrix(matrix)

   #step 3: subtract multiple of first row = 0 
   new_Ma = []
   for i in range(0,row,1):
      multiple = matrix[i][0] / matrix[0][0]
      for n in range(0,column,1):
         temp =[]
         temp += [matrix[i][n] - multiple*matrix[0][n]]
      new_Ma += [temp]
      print(new_Ma)
   matrix = new_Ma
printMatrix(matrix) 

def printMatrix(matrix):
   row =3
   for i in range (0,row,1):
      print(matrix[i])
   print("-----------------------")



matrix = [[0,3,7,9],[2,3,6,0],[8,6,8,0]]
ge_fw(matrix)
      



#|0 3 7 9|   
#|2 3 6 0|
#|8 6 8 0|
#
#
#|2 3 6 0|
#|0 3 7 9|   
#|8 6 8 0|
#
#R3 -4R1
#|2  3  6    0|
#|0  3  7    9|   
#|0 -6 -16 -36|


#def ge_bw(matrix):
