import random
from convexHullFinalV3NGph import generarConvexHull, Punto
import matplotlib.pyplot as plt

def readFile():
    puntos_unicos=set()
    with open("campo.in","r") as f:
        lineas = f.readlines()
        for linea in lineas[:-1]:  # todas menos la última
            x, y = map(int, linea.split())
            puntos_unicos.add((x, y))
    lista_puntos = [Punto(x, y) for x, y in puntos_unicos]#Conv a obj Punto
    lista_puntos.sort(key=lambda p: (p.x, -p.y))#Ordenarlos (x ascendente, y descendente)
    return lista_puntos

def generarPuntosAleat(limiteInf:int = 0, limiteSup:int = 10, cantidad:int = 10):
    # 10 puntos con coordenadas enteras (los limites se incluyen)
    puntos_unicos = set()
    while len(puntos_unicos) < cantidad:
        x = random.randint(limiteInf, limiteSup)
        y = random.randint(limiteInf, limiteSup)
        puntos_unicos.add((x, y))
    lista_puntos = [Punto(x, y) for x, y in puntos_unicos]#Conv a obj Punto
    lista_puntos.sort(key=lambda p: (p.x, -p.y))#Ordenarlos (ascendente en x, descendente en y)
    return lista_puntos

def calcularArea(a,b,c):
    # retorna el doble del área del triángulo
    return abs((b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x))

def findMaxArea(convexHull):
    areaMax=0
    puntosAreaMax=[]
    for i in range(len(convexHull)-2):#Dejar espacio para los otros dos puntos (j,k)
        for j in range(i+1,len(convexHull)-1): # Dejar espacio para k
            for k in range(i+2,len(convexHull)): 
                areaActual=calcularArea(convexHull[i],convexHull[j],convexHull[k])
                if areaActual>areaMax: 
                    areaMax=areaActual
                    puntosAreaMax=[convexHull[i],convexHull[j],convexHull[k]]
    return puntosAreaMax

def generarOutputFile(puntosAreaMax: list[Punto]):
    with open("campo.out","w") as f:
        for p in puntosAreaMax:
            f.write(str(p.x)+" "+str(p.y)+"\n")

# Dibujar
def dibujarGrafico(pilaConvexHull, listaPtosTrian:list):
    fig, ax = plt.subplots()
    dibujarPuntos(ax)
    for i in range(len(pilaConvexHull)-1):
        dibujarLinea(pilaConvexHull[i],pilaConvexHull[i+1],ax)
        plt.draw()
    dibujarLinea(pilaConvexHull[-1],pilaConvexHull[0],ax)
    dibujarTriangulo(listaPtosTrian,ax)
    plt.show()

def dibujarPuntos(ax):
    for punto in lista_puntos:
        #ax.scatter(punto.x,punto.y,color="red")
        punto.plotObj,=ax.plot(punto.x,punto.y, 'o', color='red')
        plt.draw()

def dibujarLinea(p1:Punto,p2:Punto, ax, color="blue"):
    ax.plot([p1.x,p2.x],[p1.y,p2.y],color=color)

def dibujarTriangulo(listaPtosTrian:list,ax):
    dibujarLinea(listaPtosTrian[0],listaPtosTrian[1],ax,"green")
    dibujarLinea(listaPtosTrian[1],listaPtosTrian[2],ax,"green")
    dibujarLinea(listaPtosTrian[2],listaPtosTrian[0],ax,"green")

# Main
lista_puntos=readFile()
miConvexHull=generarConvexHull(lista_puntos)
print(miConvexHull)
listaTriangulo=findMaxArea(miConvexHull)
print(listaTriangulo)
generarOutputFile(listaTriangulo)

dibujarGrafico(miConvexHull,listaTriangulo)