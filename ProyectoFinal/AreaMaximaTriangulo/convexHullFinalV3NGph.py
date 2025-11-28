# NGPh significa no-graficos (no muestra graficos).

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.plotObj=None
    def __repr__(self):
        return "P("+str(self.x)+", "+str(self.y)+")"

def productoPunto(v1,v2):
    return v1.x*v2.x+v1.y*v2.y

def proyVec(v1:Punto,v2:Punto): #Sigue la formula: (v1*v2/(v2*v2))*v
    arriba=productoPunto(v1,v2)
    abajo=productoPunto(v2,v2)
    division=arriba/abajo
    x=division*v2.x
    y=division*v2.y
    return Punto(x,y)

def createVec(A:Punto, B:Punto):
    return Punto(B.x-A.x,B.y-A.y)

def getFinalPP(A:Punto,B:Punto,C:Punto):
    VAB=createVec(A,B)
    VAC=createVec(A,C)
    PP=proyVec(VAB,VAC)
    return Punto(A.x+PP.x,A.y+PP.y)

def isPartOfConvexHull(A:Punto,B:Punto,C:Punto,upOrDown:str):
    PP=getFinalPP(A,B,C)
    if upOrDown=="up":
        if B.y>PP.y: return True
        return False
    else:
        if B.y<PP.y: return True
        return False

# Algoritmo Convex Hull
def generarCH_UP(lista_puntos:list[Punto]):
    pilaConvexHullUp=[]
    pilaConvexHullUp.append(lista_puntos[0])#Los extremos simpre seran parte del CH
    i=0
    while i+2<len(lista_puntos):#Hay 3 puntos para evaluar
        if isPartOfConvexHull(lista_puntos[i],lista_puntos[i+1],lista_puntos[i+2],"up"):# Evaluar el de en medio
            pilaConvexHullUp.append(lista_puntos[i+1])
            if len(pilaConvexHullUp)>=3:
                #Comprobar que los puntos anteriores siguen siendo parte del CH
                eliminoUnPunto=True
                while eliminoUnPunto and len(pilaConvexHullUp)>=3:
                    eliminoUnPunto=False
                    if not isPartOfConvexHull(pilaConvexHullUp[-3],pilaConvexHullUp[-2],pilaConvexHullUp[-1],"up"):
                        #Cambiar bandera
                        eliminoUnPunto=True
                        #Eliminar falso miembro del CH
                        aux=pilaConvexHullUp.pop()#Este si es miembro
                        pilaConvexHullUp.pop()#Falso miembro
                        pilaConvexHullUp.append(aux)#Agregar ultimo miembro
        i+=1
        
    #Aniadir ultimo punto y comprobar
    pilaConvexHullUp.append(lista_puntos[-1])#Los extremos simpre seran parte del CH
    #Comprobar que los puntos anteriores siguen siendo parte del CH
    eliminoUnPunto=True
    while eliminoUnPunto and len(pilaConvexHullUp)>=3:
        eliminoUnPunto=False
        if not isPartOfConvexHull(pilaConvexHullUp[-3],pilaConvexHullUp[-2],pilaConvexHullUp[-1],"up"):
            #Cambiar bandera
            eliminoUnPunto=True
            #Eliminar falso miembro del CH
            aux=pilaConvexHullUp.pop()#Este si es miembro
            pilaConvexHullUp.pop()#Falso miembro
            pilaConvexHullUp.append(aux)#Agregar ultimo miembro
    return pilaConvexHullUp
 
def generarCH_Down(lista_puntos:list[Punto]):
    pilaConvexHullDown=[]
    pilaConvexHullDown.append(lista_puntos[-1])#Los extremos simpre seran parte del CH
    i=len(lista_puntos)-1
    while i-2>=0:
        if isPartOfConvexHull(lista_puntos[i],lista_puntos[i-1],lista_puntos[i-2],"down"):
            pilaConvexHullDown.append(lista_puntos[i-1])
            if len(pilaConvexHullDown)>=3:
                #Comprobar que los puntos anteriores siguen siendo parte del CH
                eliminoUnPunto=True
                while eliminoUnPunto and len(pilaConvexHullDown)>=3:
                    eliminoUnPunto=False
                    if not isPartOfConvexHull(pilaConvexHullDown[-3],pilaConvexHullDown[-2],pilaConvexHullDown[-1],"down"):
                        #Cambiar bandera
                        eliminoUnPunto=True
                        #Eliminar falso miembro del CH
                        aux=pilaConvexHullDown.pop()#Este si es miembro
                        pilaConvexHullDown.pop()#Falso miembro
                        pilaConvexHullDown.append(aux)#Agregar ultimo miembro
        i-=1

    #Aniadir ultimo punto y comprobar
    pilaConvexHullDown.append(lista_puntos[0])#Los extremos simpre seran parte del CH
    #Comprobar que los puntos anteriores siguen siendo parte del CH
    eliminoUnPunto=True
    while eliminoUnPunto and len(pilaConvexHullDown)>=3:
        eliminoUnPunto=False
        if not isPartOfConvexHull(pilaConvexHullDown[-3],pilaConvexHullDown[-2],pilaConvexHullDown[-1],"down"):
            #Cambiar bandera
            eliminoUnPunto=True
            #Eliminar falso miembro del CH
            aux=pilaConvexHullDown.pop()#Este si es miembro
            pilaConvexHullDown.pop()#Falso miembro
            pilaConvexHullDown.append(aux)#Agregar ultimo miembro
    return pilaConvexHullDown

def unirCadenasCH(pilaConvexHullUp:list ,pilaConvexHullDown:list): # UNIR AMBAS CADENAS (UP Y DOWN)
    pilaConvexHull=[]
    #Eliminar extremos para que no haya duplicados
    pilaConvexHullUp.pop()#Elimina el extremo derecho de los puntos
    pilaConvexHullDown.pop()#Elimina el extreom izquierdo(inicio) de los puntos
    pilaConvexHull.extend(pilaConvexHullUp)
    pilaConvexHull.extend(pilaConvexHullDown)
    return pilaConvexHull

def generarConvexHull(lista_puntos:list[Punto]):
    cadenaCHUP=generarCH_UP(lista_puntos)
    cadenaCHDOWN=generarCH_Down(lista_puntos)
    return unirCadenasCH(cadenaCHUP,cadenaCHDOWN)
