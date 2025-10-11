a=[-9,3,5,-2,9,-7,4,8,6]

def buscarFactores(a):
    maxProducto=0
    factores=[]
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i]*a[j] > maxProducto and i!=j: 
                maxProducto=a[i]*a[j]
                factores=[a[i],a[j]]
    return factores

print(buscarFactores(a))
