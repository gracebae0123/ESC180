L=range(1,10,1)
print(list(L))

def square(x):
    return x*x

M=map(square,L)
print(list(M))

def reducingSum(a,b):
    return a+b

def reduce(fn,x):
    isOddidx = True
    sum=[]
    for i in range (0,len(x)-2,1):
        if isOddidx == True:
            sum += [reducingSum(x[i],x[i+1])]
            isOddidx = False
            print (sum)
        else:
            isOddidx = True
    if len(x) %2 !=0:
        sum += [x[-1]]
    print (sum)
#   result = map(fn,sum) 
    return sum 

msum=reduce(reducingSum,M)
print (str(msum))


def reduce(fn,x):
    for i in range (0,len(x)-2,1):
        
