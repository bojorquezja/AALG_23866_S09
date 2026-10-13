def mergesort(a):
    n = len(a)
    if n <= 1:   
        return a
    mitad = n // 2
    arrayOne = a[:mitad]            
    arrayTwo = a[mitad:]          
    arrayOne = mergesort(arrayOne)  
    arrayTwo = mergesort(arrayTwo)
    return merge(arrayOne, arrayTwo)

def merge(a, b):
    c = []

    while len(a) > 0 and len(b) > 0:     
        if a[0] > b[0]:
            c.append(b[0])              
            b.pop(0)                   
        else:
            c.append(a[0])
            a.pop(0)

    while len(a) > 0:
        c.append(a[0])
        a.pop(0)

    while len(b) > 0:
        c.append(b[0])
        b.pop(0)
    return c
numeros = [14, 7, 3, 12, 9, 11, 6, 2]
print("Original:", numeros)
print("Ordenado:", mergesort(numeros))