def revisaSuma(data,k):##Funcion que recibe una lista y un numero.
    for i in data: #Dos for anidados que recorren el arreglo.
        for j in data: 
            if i+j==k: return (i,j) #Regresa los sumandos en caso de hayarlos.
    return None #En caso de no hayar los sumandos retorna None.

print(revisaSuma([0,1,2,3],9))