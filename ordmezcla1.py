
def mezcla(a, izq, centro, der):
    i = izq
    j = centro + 1
    auxiliar = []

    while i <= centro and j <= der:
        if a[i] <= a[j]:
            auxiliar.append(a[i])
            i += 1
        else:
            auxiliar.append(a[j])
            j += 1

    while i <= centro:
        auxiliar.append(a[i])
        i += 1

    while j <= der:
        auxiliar.append(a[j])
        j += 1

    for k in range(len(auxiliar)):
        a[izq + k] = auxiliar[k]


def ordenamientoMezcla(a, izq, der):
    if izq >= der:
        return

    centro = (izq + der) // 2

    ordenamientoMezcla(a, izq, centro)
    ordenamientoMezcla(a, centro + 1, der)

    mezcla(a, izq, centro, der)


a = []

for i in range(6):
    numero = int(input(f"ingrese el numero {i + 1}: "))
    a.append(numero)

print("lista original:", a)

ordenamientoMezcla(a, 0, len(a) - 1)

print("lista ordenada:", a)