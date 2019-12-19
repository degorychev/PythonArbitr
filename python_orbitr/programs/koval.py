import sys

def Koval(s):
    a={}
    ch=0
    nech=0
    
    for i in range(len(s)):a.update({s[i]:1}) if a.get(s[i])==None else a.update({s[i]:int(a.get(s[i]))+1})
    for i in a.keys():
        if int(a.get(i))%2==0:ch=ch+1
        else:nech=nech+1   
    k=len(s)
    #РЅРµС‡РµС‚РЅРѕРµ РєРѕР»РёС‡РµСЃС‚РІРѕ СЃРёРјРІРѕР»РѕРІ
    if k%2!=0:
        if nech%2!=0 and ch==0:
            for i in a.keys():return str(i)+" SYMBOL"
        elif nech%2!=0 and ch!=0:
            for i in a.keys():
                if int(a.get(i))%2==0:
                    return str(i)+" GROUP"
        else:
            for i in a.keys():return str(i)+" SYMBOL"
    #С‡РµС‚РЅРѕРµ РєРѕР»РёС‡РµСЃС‚РІРѕ СЃРёРјРІРѕР»РѕРІ    
    else:
        
        #РїРѕРІС‚РѕСЂСЏСЋС‚СЃСЏ С‡РµС‚РЅС‹Рµ РЅРµС‡РµС‚РЅРѕРµ РєРѕР»РёС‡РµСЃС‚РІРѕ СЂР°Р·    
        if nech%2==0 and ch%2!=0:
            for i in a.keys():
                if int(a.get(i))%2==0:
                    return str(i)+" GROUP"
        #РїРѕРІС‚РѕСЂСЏСЋС‚СЃСЏ С‡РµС‚РЅС‹Рµ С‡РµС‚РЅРѕРµ РєРѕР»РёС‡РµСЃС‚РІРѕ СЂР°Р·        
        elif nech%2==0 and ch%2==0:
            for i in a.keys():
                if int(a.get(i))!=0:
                    return str(i)+" SYMBOL"
        #РїРѕРІС‚РѕСЂСЏРµС‚СЃСЏ РєР°Р¶РґС‹Р№ РЅРµС‡РµС‚РЅРѕРµ РєРѕР»РёС‡РµСЃС‚РІРѕ СЂР°Р·
        elif nech%2==0 and ch==0:
            for i in a.keys():return str(i)+" SYMBOL"         
        else:
            for i in a.keys():
                return str(i)+" GROUP"        
               
        
    

s=sys.argv[1]
print(Koval(s))