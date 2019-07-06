def fibo(n): #return nth fibonacci num
    if (n==0) or (n==1):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fiboL(n): #return list of up to nth fibo num
    accum=[]
    for i in range (0,n,1):
        accum += [fib(i)]
    return accum

def redfibo(n):
    result = map (reduce,
