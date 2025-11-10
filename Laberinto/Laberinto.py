import csv

# FORMATO: x, y
IZQ=[-1,0]
DER=[1,0]
ARRIBA=[0,-1]
ABAJO=[0,1]

laberinto=[]
pilaDeMov=[]
deadEnds=[]
finalizar=False
tieneSolucion=False

def leerArchivo():
    with open('entrada.txt', newline='') as archivo:
        lector = csv.reader(archivo)
        filas = list(lector)
        
        for fila in range(2,len(filas)):
            renglon=[]
            for element in range(len(filas[2])):
                renglon.append(filas[fila][element])
            laberinto.append(renglon)

def revisar(direccion): # retorna true, si hubo movimiento
    global finalizar, tieneSolucion

    seMovio=False
    posARevisar=None
    
    try:
        posActual=pilaDeMov[-1] #Recuperar pos actual
        #Definir pos a revisar
        X=posActual[0]+direccion[0]
        Y=posActual[1]+direccion[1]
    except IndexError:
        #la pila de mov esta vacia (no hay solucion)
        pass
    
    try:
        if X >= 0 and Y >= 0:#Evitar que py use valores negativos
            posARevisar=laberinto[Y][X]
    except:#No se creo X e Y, la pila esta vacia, sin solucion
        pass

    if posARevisar == "0":
        if [X,Y] not in pilaDeMov and [X,Y] not in deadEnds:#Hay camino nuevo
            pilaDeMov.append([X,Y])
            seMovio=True
    elif posARevisar == "S":#Encontro la salida
            pilaDeMov.append([X,Y])
            finalizar=True
            tieneSolucion=True
    return seMovio
        
def explorarVecinosRecursivamente():
    global finalizar

    if not finalizar:
        if revisar(IZQ): explorarVecinosRecursivamente()
        if revisar(DER): explorarVecinosRecursivamente()
        if revisar(ARRIBA): explorarVecinosRecursivamente()
        if revisar(ABAJO): explorarVecinosRecursivamente()
        #si llego hasta aqui es porque no se movio
        #si no, hubiera continuado explorando
        if not finalizar:
            try:#Verificar que no se haga un pop de la pila estando vacia
                deadEnds.append(pilaDeMov.pop())
                explorarVecinosRecursivamente()
            except IndexError:#si la pila esta vacia, todos los caminos son dead end, no hay solucion
                finalizar=True
    
def mostrarResultados():
    if tieneSolucion:
        print("FINALIZADO!!\nSolucion:\n",pilaDeMov)
    else:
        print("El laberinto no tiene Solucion")
    
def encontrarEntrada():
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j]=="E":
                pilaDeMov.append([j,i])
                return True
    print("El laberinto no tiene entrada (E)")
    return False
    

print("\n--------------El txt de entrada debe contener en el primer renglon filas y en el segundo columnas :D------------\n\n")
leerArchivo()
if encontrarEntrada():
    explorarVecinosRecursivamente()
    mostrarResultados()