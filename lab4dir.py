def imprime(mat):
    for x in mat:
        print(x)
    print()

def valido(lab, res, f, c):
    if f >= len(lab):
        return False
    if f < 0:
        return False
    if c >= len(lab[0]):
        return False
    if c < 0:
        return False
    if res[f][c] == 1:
        return False
    if lab[f][c] == 0:
        return False
    return True

def laberB(lab, res, f, c):
    if f == len(lab) - 1 and c == len(lab[0])-1:
        if valido(lab, res, f, c):
            res[f][c] = 1
            
            imprime(res)
            return True
        else:
            return False
    else:
        if valido(lab, res, f, c):
            res[f][c] = 1
            imprime(res)
            if laberB(lab, res, f+1, c):
                return True
            elif laberB(lab, res, f, c+1):
                return True
            elif laberB(lab, res, f-1, c):
                return True
            elif laberB(lab, res, f, c-1):
                return True
            else:
                res[f][c] = 0
                return False
        else:
            return False

lab = [
    [1,1,1,1,0,1,1,1,1],
    [1,0,0,1,0,1,0,0,0],
    [1,1,0,1,1,1,1,0,1],
    [0,1,0,1,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,1,0,1],
    [1,1,1,1,0,1,1,0,1],
    [1,0,0,1,0,1,0,0,1],
    [1,1,1,1,0,1,1,1,1]
]
res = [[0 for _ in range(9)] for _ in range(9)]

if laberB(lab, res, 0, 0):
    print("Salimos!")
else:
    print("Quedamos atrapados")

