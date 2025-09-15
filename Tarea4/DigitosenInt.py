def contarDigitosenInt(entero:int)->int:
    if entero==0:
        return 0
    else:
        return 1+contarDigitosenInt(int(entero/10))
    
print(contarDigitosenInt(1))