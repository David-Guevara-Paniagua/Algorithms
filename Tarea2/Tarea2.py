def buscar(data,num):           #T(n)=1     S(n)=n+1
    numDeComparaciones=0        #T(n)=1     S(n)=1
    for item in data:           #T(n)=n     S(n)=1
        numDeComparaciones+=1   #T(n)=1     S(n)=0
        if item==num: break     #T(n)=1     S(n)=0
    return numDeComparaciones   #T(n)=1     S(n)=0

print("Comparaciones:",buscar([0,1,2,3,4],9))