def bubblesort(inlist):
   i =0
   swapped = False 
   temp = 0
   j =0
   for i in range(len(list)-1,0,-1): 
      for j in range(i):
      for (j<len(array)):
         if list[j] > list[j+1]:
            temp =list[j]
            list[j] = list[j+1]
            list[j+1] = temp
            swapped = True
   if swapped == True:
      return [True, array]
   else:
      return [False,array]

size = 5
array[5] = [1,4,5,3,2]
i = 0
print("=====original=====\n")
for i in range(0,size,1):
   print(str(array[i])


bubblesort(array)
print("=====new====\n")
print(str(array))
