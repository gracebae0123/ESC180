#def halloween_reaction(thing):
#   if (thing == "ghotst") or (thing == "monster") or (thing == midterm):
#      return "NOO!"
#   else:
#      return "YAY!"
#
#def print_mid_part(L):
#   print (L[1:len(L)-1])
#
#print_mid_part(["pumpkins","candy","costumes","autumn", "zombies"])
#
#def h(L):
#   L = ["fall","colours"]
#   return L
#
#def odds_sum(L):
#   sum = 0
#   for num in L:
#      if num %2 == 1:
#         sum += num
#   return sum
#
#print(str(odds_sum([1,3,4,5])))
#
#i = 5
#while i < 500:
#   print (i)
#   i+=3

def kids_who_like_candy(faves,kids):
   result = []
   for i in range (0,len(faves),1):
      if faves[i] == "candy":
         result = result +[kids[i]]
   return result

faves = ["candy","costumes","weather","candy"]
kids = ["Bob","Dorothy","Mike", "Alice"]

print(kids_who_like_candy(faves,kids)) 
   
def halloween_surprise():
   output = [3,2,1,"SURPRISE!"]
   
