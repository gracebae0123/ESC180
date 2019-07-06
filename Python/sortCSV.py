import sys
def genSortKey(col,direction):
   def key(x):
      if (direction == '+'):
         return x[col]
      else:
         return -x[col]
   return key


def main():
   FIN=[]
   FOUT=""
   nargs=len(sys.argv)
   skip=False
   for i in range(1,nargs):
      if not skip:
          arg=sys.argv[i]
          print("INFO: processing",arg)
          if arg == "--fin":
             if i != nargs-1:
                FIN=sys.argv[i+1]
                skip=True

          elif arg == "--fout":
             if i != nargs-1:
                FOUT=sys.argv[i+1]
                skip=True

          elif arg=="--col":
             if i != nargs-1:
                col=int(sys.argv[i+1])
                skip=True

          elif arg=="--dir": 
             if i != nargs-1:
                direction=sys.argv[i+1]
                skip=True

          else:
             print("ERR: unknown arg:",arg)
      else:
         skip=False

   try:
      f=open('data','r')
#   except:
#      print("ERR: file",FIN,"is not present or can't be opened")

      lines=f.readlines()
      f.close()
      accum=[]
      for i in lines:
         j=i.split('\n')[0]  
         k=j.split(',')      
         r=[]
         for x in k:
            r = r + [float(x)]
         accum = accum + [r]
      print(accum)
   

#     if (dir == '+'):
#         isRev = False
#     else:
#         isRev = True
      try:
        sortKey = genSortKey(col,direction)      
        accum = sorted(accum,key=sortKey)# reverse=isRev)
           
        # print (sort)
        try:
           g=open(FOUT,'w')
           isFirst =True
           for i in accum:
              for n in i:
                 if (isFirst):
                    g.write(str(n))
                    isFirst=False
                 else:
                    g.write(","+str(n))
                    g.write("\n")    
                    isFirst=True
           g.close()
        except:
           print(sys.exc_info())
           print("ERROR:File",FOUT,"cannot be opened")
      except:
         print(sys.exc_info())
         print("wrong value(s) entered for column and/or direction")
   except:
      print(sys.exc_info())
      print("ERROR: file",FIN,"is not present or can't be opened")
      
   return True

main()

