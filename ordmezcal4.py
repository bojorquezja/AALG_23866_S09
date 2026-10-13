#division
def mergesort(lista):
    if len(lista) <=1:
        return lista
    
    mid = len(lista)//2
    izq= mergesort(lista[:mid])
    der= mergesort(lista[mid:])
    
    return merge(izq,der)

#ordenamiento
def merge(izq,der):
    result = []
    i=0
    j=0
    while i < len(izq) and j < len(der):
        if izq[i]<der[j]:
            result.append(izq[i])
            i+=1
        else:
            result.append(der[j])
            j+=1
    
    result.extend(izq[i:])
    result.extend(der[j:])
    return result

datos = [14, 7, 3, 12, 9, 11, 6, 2]
print(mergesort(datos))