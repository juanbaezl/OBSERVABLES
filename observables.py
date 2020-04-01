import numpy as np
from libreria import *

def probabilidad(vect1,vect2):
    res = interno(vect2,vect1)
    total = (mod(res))**2
    return total
#4.3
def primero(vect, exponente):
    init = [[(0,1),(1,0)],[(0,-1),(1,0)],[(1,0),(1,0)],[(-1,0),(1,0)],[(0,0),(1,0)],[(1,0),(0,0)]]
    total = []
    for i in range((exponente*2)-2,exponente*2):
        if probabilidad(vect,init[i])!= 0.0:
            total = total + init[i]
    return total
def segundo(vect, exponente):
    matriz = [[[(1,0),(0,0)],[(0,0),(-1,0)]],[[(0,0),(0,-1)],[(0,1),(0,0)]],[[(0,0),(1,0)],[(1,0),(0,0)]]]
    propios = []
    res = primero(vect, exponente)
    prob = []
    total =[]
    for i in range(len(aux)):
        prob = prob + probabilidad(a, res[i])
    for i in range(3):
        valor,no = np.linalg.eig(matriz[i])
        propios = propios + valor
    for i in range(2):
        total = total + (prob[i]*propios[exponente][i])
    return total
#4.4
def tercero():
    h = (2**(1/2))/2
    mat1 = [[(0,0),(1,0)],[(1,0),(0,0)]]
    mat2 = [[(h,0),(h,0)],[(h,0),(-h,0)]]
    if unitaria(mat1) and unitaria(mat2):
        res = multimat(mat1,mat2)
        return unitaria(res)
def cuarto():
    h = 1/ (2**(1/2))
    matriz =[[(0,0),(h,0),(h,0),(0,0)],[(0,h),(0,0),(0,0),(h,0)],[(h,0),(0,0),(0,0),(0,h)],[(0,0),(h,0),(-h,0),(0,0)]]
    vect = [(1,0),(0,0),(0,0),(0,0)]
    for i in range(3):
        vect = accion(matriz,vect)
        vectres =vect[3]
    prob = (mod(vectres))**2
    return prob
