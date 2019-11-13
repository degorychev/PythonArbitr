import sys

def Losev(s):
    a={}
    chet=0
    nechet=0
    for i in range(len(s)):a.update({s[i]:1}) if a.get(s[i])==None else a.update({s[i]:int(a.get(s[i]))+1})
    for i in a.keys():
        if int(a.get(i))%2==0:chet=chet+1
        else:nechet=nechet+1
    if chet%2==0 and nechet%2==0:
        for i in a.keys():return str(i)+" SYMBOL"
    elif chet==0 and nechet%2!=0 or chet%2==0 and nechet%2!=0:
        for i in a.keys():
            if int(a.get(i))%2!=0:return str(i)+" GROUP"
        #print("DROP NECHET GROUPE")
    elif nechet==0 and chet%2!=0 or nechet%2==0 and chet%2!=0:
        for i in a.keys():
            if int(a.get(i))%2==0:return str(i)+" GROUP"
        #print("DROP CHET GROUPE")
    elif chet%2!=0 and nechet%2!=0:
        for i in a.keys():
            if int(a.get(i))%2==0:return str(i)+" SYMBOL"
        #print("DROP SYMBOL WITH CHET GROUPE")
    else:
        return "BAG"

s=sys.argv[1]
print(Losev(s))