def ordenamientoMezcla(lista):
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2

    listaIzquierda = lista[:mitad]
    listaDerecha = lista[mitad:]

    listaIzquierda = ordenamientoMezcla(listaIzquierda)
    listaDerecha = ordenamientoMezcla(listaDerecha)

    return mezclar(listaIzquierda, listaDerecha)


def mezclar(listaIzquierda, listaDerecha):
    listaCombinada = []

    while len(listaIzquierda) > 0 and len(listaDerecha) > 0:
        if listaIzquierda[0] > listaDerecha[0]:
            listaCombinada.append(listaDerecha.pop(0))
        else:
            listaCombinada.append(listaIzquierda.pop(0))

    while len(listaIzquierda) > 0:
        listaCombinada.append(listaIzquierda.pop(0))

    while len(listaDerecha) > 0:
        listaCombinada.append(listaDerecha.pop(0))

    return listaCombinada


numeros = input("Ingrese los números separados por comas: ").split(",")
numeros = [int(num) for num in numeros]
resultado = ordenamientoMezcla(numeros)
print("Lista ordenada:", resultado)