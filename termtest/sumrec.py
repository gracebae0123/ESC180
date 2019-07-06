#def sumRec(n):
#   sum = 0
#   if type(n) == int:
#      if n>= 0:
#         if n==0:
#            return 1
#         elif n>0:
#            sum = sum + sumRec(n-1)
#            return (n+1+sum)
#      else:
#         return False
#   else:
#      return False
#
#print (str(sumRec(3)))
#
#
#
#def sumRec(n):
#   sum =0
#   if type(n) == int:
#      if n ==0:
#         return 1
#      elif n>0:
#         sum = sum +sumRec(n-1)
#         return (n+1+sum)
#   else:
#      return False
#
#print (str(sumRec(3)))
#
#
#def reverseDouble(word):
#   result =""
#   for i in range (len(word)-1,-1,-1):
#      result =  result +word[i] + word[i]
#   return result
#
#print (reverseDouble("Apple")) 

#def sumLoop(n):
#   sum = 0
#   for num in range (0,n+2,1):
#      sum = sum + num 
#   return sum
#print (str(sumLoop(3)))

class counter:
   def __init__(self):
      self.cnt = 0
      self.incr = 0
   def setCnt(self,counter):
      self.cnt = counter
      return True
   def setIncrement(self,incre):
      self.incr = incre
      return True
   def getCnt(self):
      return self.cnt
   def count(self):
      self.cnt = self.cnt + self.incr
      return True
 
