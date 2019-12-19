import sys
#import collections
import random
import re
 
def countChar1(text):
    res = {}  
    chetn_gruppi = 0
    nechetn_gruppi = 0
    
    for c in text:
        if c not in res:
            res[c] = 1
        else:
            res[c] += 1
    #for key, value in res.items():
        #print(key, value)
    for value in res.values():
      if value%2==0:
        chetn_gruppi+=1
      else: nechetn_gruppi+=1  
    #print("Нечетных групп — ", nechetn_gruppi,"Четных групп — ", chetn_gruppi)
    if chetn_gruppi%2==0 and nechetn_gruppi%2==0 or nechetn_gruppi%2==0 and chetn_gruppi%2==0: 
        return( random.choice(list(res.keys())))
    elif chetn_gruppi%2==0 and nechetn_gruppi%2!=0 or nechetn_gruppi%2!=0 and chetn_gruppi%2==0:
      for key, value in res.items(): 
        if value%2!=0:
          return(key+" SYMBOL")
    elif nechetn_gruppi%2!=0 and chetn_gruppi%2!=0 or chetn_gruppi%2!=0 and nechetn_gruppi%2!=0:
      for key, value in res.items(): 
        if value%2==0:
         return(key+" SYMBOL")
    elif chetn_gruppi%2!=0 and nechetn_gruppi%2==0 or nechetn_gruppi%2==0 and nechetn_gruppi%2==0:
      for key, value in res.items(): 
        if value%2==0:
         return(key+" GROUP")
    elif nechetn_gruppi%2!=0 or chetn_gruppi%2!=0:
      for key, value in res.items(): 
         return(key+" GROUP") 
    elif nechetn_gruppi%2==0 or chetn_gruppi%2==0:
      for key, value in res.items(): 
         return(key+" SYMBOL")           
    else:  
        for key, value in res.items(): 
         return(key+" SYMBOL")
    
text=sys.argv[1]
print(countChar1(text))