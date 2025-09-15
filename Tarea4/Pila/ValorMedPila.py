from Tarea4.Pila.Stack import *

def eliminarMedioRec(pila:Stack,stopIn:int):
    value=pila.pop()
    if stopIn != 0:
        eliminarMedioRec(pila,(stopIn-1))
        pila.push(value)

def eliminarMedio(pila:Stack):
    eliminarMedioRec(pila,int(len(pila)/2))

#Crear pila y llenarla
myStack=Stack()
for x in range(21): myStack.push(x+1)

#Llamar a la funcion
print(myStack)
eliminarMedio(myStack)
print("---")
print(myStack)