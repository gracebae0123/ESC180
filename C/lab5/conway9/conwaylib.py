import random
from rule import rule
class conway:
   def __init__(self,sublistNum,sublistSize,condition):
      self.list =[]
      self.sublistNum = sublistNum
      self.sublistSize = sublistSize
      for dummy in range(0,self.sublistNum,1):
         temp = []
         for dummy2 in range(0,self.sublistSize,1):
            if condition == "random":
               temp += [random.randint(0,1)]
            elif condition == "zeros":
               temp +=[0]
            else:
               temp += [1]
         self.list+= [temp]

   def getDisp(self):
      result =""
      for i in range(0,self.sublistNum,1):
         for n in range(0,self.sublistSize,1):
            if self.list[i][n] == 0:
               result += " "
            else:
               result += "*"
         result +="\n"
      return result

   def printDisp(self):
      print(self.getDisp())
      return True

   def setPos(self,row,col,val):
      if (val == 0) or (val == 1):
         self.list[row][col] = val
        return True
      else:
         return False

   def getNeighbours(self,row,col):
      result = [
                self.list[(row-1)%self.sublistSize][(col-1)%self.sublistNum], #(-.-)
                self.list[(row-1)%self.sublistSize][(col  )%self.sublistNum],
                self.list[(row-1)%self.sublistSize][(col+1)%self.sublistNum],

                self.list[(row  )%self.sublistSize][(col-1)%self.sublistNum],
                self.list[(row  )%self.sublistSize][(col+1)%self.sublistNum],

                self.list[(row+1)%self.sublistSize][(col-1)%self.sublistNum],
                self.list[(row+1)%self.sublistSize][(col  )%self.sublistNum],
                self.list[(row+1)%self.sublistSize][(col+1)%self.sublistNum]
            ]
           ]
     return result

   def evolve (self):
      state = []
      for dummy in range(0,self.sublistNum,1):
         temp = []
         for dummy2 in range(0,self.sublistSize,1):
               temp += [0]
         state += [temp]
      for dummy in range(0,self.sublistNum,1):
         for dummy2 in range(0,self.sublistSize,1):
            state[dummy][dummy2] = [rule(self.list[dummy][dummy2]),getNeighbours(dummy,dummy2)]
      return true
      

 


#x=conway(4,4,'zeros')
#print(x.list)
#x.printDisp()
#print(x.getNeighbours(3,0))
 

