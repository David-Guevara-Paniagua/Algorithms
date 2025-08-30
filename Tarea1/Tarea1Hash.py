def revisarSuma(data,k): #Funcion que recibe una lista y un numero.
    vistos=set() #ED tipo set (conjunto) que usa hash para almacenar los datos.
    for i in data:
        vistos.add(i)
        diferencia=k-i
        if diferencia in vistos: return (i,diferencia) #Regresa los sumandos en caso de hayarlos.
    return None #En caso de no hayar los sumandos retorna None.
        

print(revisarSuma([0,1,2,3],7))