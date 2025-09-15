def sumaRe(lista:list)->int:
    if len(lista) == 0:
        return 0
    else:
        return sumaRe(lista[:-1])+lista[-1]

print(sumaRe([]))
