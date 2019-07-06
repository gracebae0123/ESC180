1. 
a)number, sequential,boolean
b)+,==
c)defining functions, creating classes
d) function that calls itself
e)if/elif/else, while,for
f)infinite loop may occur
g)insert print statements to see the process
h)def name(arg) arguments list, return
i)if the two results have the same type, then it is hard to isolate the two when returned
  you can return more than one value via a single return coupled with a return value
j)data structure is the arrangement and exploitation of the underlying data types of a language to map to a real-world problem
  This is important because ...
k)x is not a sequential type
l)n is not an integer--> convert by int(n)
m)raw_input(input from users) and print(diplay to the user)
n)recursive function may not have base case or never hit this case. 
o)accumulator is a variable that stores a value that is continuously modified. It is used when one is formulating a mathematical algorithm 
 when the....

2. if and if--elif are not equivalent
   e.g. x=10
        if x>0:
            return print("x>10")
        if x==10:
            return print("x==10")
        ---> this will print both "x>10" and "x==10"

        HOWEVER,
        if x>0:
            return print("x>10")
        elif x==10:
            return print("x==10")
        ---> this will print only "x>10" because this is the first statement that is true --> no need to check the next one

3. If the input x is equal to 0, the function returns 0. 
   If the input is even, it returns a sum of even numbers from 0 to the number.
   If the input is odd, the function runs infinitely

4. def reverseDouble(word):
        accum=[]
        for i in range(len(word)-1,-1,-1):
            accum+=word[i]+word[i]
        return accum

5. def sumLoop(n):
    sum=0
    if type(n) == int:
        if n>=0
        for num in range (0,n+1,1):
            sum += num
        return sum
        else:
            return False
    else:
        return False

    def sumRec(n):
        sum=0
        if type(n)==int:
            if n==0:
               return 1
            elif n >0:
                sum=sum+sumRec(n-1)
                return (n+1+sum)            
            else:
                return False
          else:
             return False
      else:
         return False


6. a) list
   b) [1,1,1,1,0,0,1]
   c)
def formDisp(x):
    if type(x) ==int:
        if x==0:
            return [1,1,1,1,1,1,0]
        elif x==1:
            return [0,1,1,0,0,0,0]
        elif x==2:
            return [1,1,0,1,1,0,1]
        else:
            return [1,1,1,1,0,0,1]
    else:
        return [1,1,1,1,1,1,0]

7.a)list of 9 elements, T/F
  b) when x: [T,F,T,F,T,F,T,F,T]
     when o: [T,T,T,T,F,T,T,T,T]
  c)
def interp(U):
    if U==[T,F,T,F,T,F,T,F,T]:
        return "X"
    elif U==[T,T,T,T,F,T,T,T,T]: 
        return "O"
    else:
        return ""

8. 
class counter:
    def __init__(self,n):
        self.count =0
        self.incre=0
    def setCnt(self,n):
        self.count =n
        return self.count
    def setIncrement(self,n):
        self.incre=n
        return self.incre
    def getCnt(self):
    def count(self):
        self.count = self.count+self.incre
        return self.count
    def getCnt(self):
        return self.count
         
