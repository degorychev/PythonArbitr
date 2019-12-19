import sys
import random
def Hawk(m):
    a={}
    even=0
    odd=0
    for i in range(len(m)):a.update({m[i]:1}) if a.get(m[i])==None else a.update({m[i]:int(a.get(m[i]))+1})
    for i in a.keys():
        if int(a.get(i))%2==0:even=even+1
        else:odd=odd+1
    if even%2==0 and odd%2==0:
        tmplist=[]
        for k in a.keys():
            tmplist.append(k)
        return random.choice(tmplist)+" symbol"
    elif even==0 and odd%2!=0 or even%2==0 and odd%2!=0:
        for i in a.keys():
            if int(a.get(i))%2!=0:return str(i)+" group"
        #print("remove odd group")
    elif odd==0 and even%2!=0 or odd%2==0 and even%2!=0:
        for i in a.keys():
            if int(a.get(i))%2==0:return str(i)+" group"
        #print("even group")
    elif even%2!=0 and odd%2!=0:
        for i in a.keys():
            if int(a.get(i))%2==0:return str(i)+" symbol"
        #print("remove letter from even group")
    else:
        return "BAG"
m=sys.argv[1]
print(Hawk(m))