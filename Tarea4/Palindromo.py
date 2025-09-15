def identificarPalin(cadena:str)->bool:
    if len(cadena)>1:
        if cadena[0]==cadena[-1]:
            return bool(True*identificarPalin(cadena[1:-1]))
        else: 
            return False
    else:
        return True

cad="reconkocer"
print(identificarPalin(cad))
    