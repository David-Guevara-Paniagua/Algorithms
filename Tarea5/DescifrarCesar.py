alfabeto="abcdefghijklmnñopqrstuvwxyz ,."

len_alfabeto=len(alfabeto)

def descrifrar(texto,desplazamiento):
    resultado=""
    for ch in texto:
        if ch in alfabeto:
            idx=alfabeto.index(ch)
            nuevoChar=alfabeto[(idx-desplazamiento)%len_alfabeto]
            resultado+=nuevoChar
    return resultado

def leerArchivo():
    with open("secreto.txt","r",encoding="utf-8") as archivoCifrado:
        textoCifrado=archivoCifrado.read()
    return textoCifrado

def puntajeEspaniol(texto):
    comunes = {"el", "la", "de", "que", "y", "a", "los", "se", 
               "en", "un", "por", "no", "es", "una", "su", "para"}
    palabrasDeTexto=texto.split()
    contador=0
    for palabra in palabrasDeTexto:
        if palabra in comunes:
            contador+=1
    return contador/len(palabrasDeTexto)

def encontrarEspaniol(listaDescifrados):
    mejorPuntaje=0
    descifradoCorrecto=None
    for descifrado in listaDescifrados:
        puntaje=puntajeEspaniol(descifrado)
        if puntaje>mejorPuntaje:
            mejorPuntaje=puntaje
            descifradoCorrecto=descifrado
    return descifradoCorrecto

def fuerzaBruta(texto):
    listaDescifrados=[]
    for i in range(len_alfabeto):
        listaDescifrados.append("DESCIFRADO "+str(i+1)+"\n"+descrifrar(texto,i+1))
        print(listaDescifrados[-1])
        print("------------------------")
    print("\n*****************************************")
    print("El descifrado correcto es:")
    print(encontrarEspaniol(listaDescifrados))
    print("\n*****************************************")

textoCifrado=leerArchivo()
fuerzaBruta(textoCifrado)
