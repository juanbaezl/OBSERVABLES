import math

def suma (a,b):
    return (a[0]+b[0], a[1]+b[1])

def prettyPrinting (a):
    print (a[0],"+",a[1],"i")

def resta (a,b):
    return (a[0] -b[0], a[1]- b[1])

def mult (a,b):
    return ((a[0]*b[0])+((-1)*a[1]*b[1]), (a[0]*b[1])+(a[1]*b[0]))

def div (a,b):
    return (((a[0]*b[0])+(a[1]*b[1]))/((b[0]*b[0])+(b[1]*b[1])), ((a[1]*b[0])- (a[0]*b[1]))/ ((b[0]*b[0])+(b[1]*b[1])))

def conjug (a):
    return (a[0], -(a[1]))

def mod (a):
    rad = (a[0]**2) + (a[1]**2)
    res = math.sqrt (rad)
    res = round (res, 2)
    return res

def pol (a,b):
    modulo = round (mod (a,b),2)
    grados = round (math.degrees(math.atan2(b,a)),2)
    return (modulo, grados )

def fase (a,b):
    res= round ((math.degrees(math.atan2(b,a))),2)
    return (res)

def addvect (a,b):
    matriz = len (a)*[([],[])]
    for i in range (0,len (a)):
        matriz[i] = suma (a[i],b[i])
    return(matriz)

def men (a):
    return (-(a[0]),-(a[1]))

def inverse (a):
    matriz =len(a)*[([],[])] 
    i=0
    for i in range (0,len(a)):
        matriz [i] = men(a[i])
    return (matriz)

def multi (a,b):
    
    return (a*b[0],a*b[1])


def escal (a,b):
    matriz = len (a)*[([],[])]
    for i in range (0,len(a)):
           matriz[i] = multi(b,(a[i]))
    return (matriz)
def conjugvect(a):
    matriz = len (a)*[([],[])]
    for i in range (0,len(a)):
           matriz[i] = conjug(a[i])
    return (matriz)
    
def addmat (a,b):
    matriz = []
    for i in range(len(a)):
        matriz.append([])
        for j in range(len(a)):
            matriz[i].append(None)
    for i in range (0,len(a)):
        for j in range (0,len(a)):
            matriz[i][j] = suma (a[i][j],b[i][j])
    return (matriz)

def invmat (a):
    matriz = []
    for i in range(len(a)):
        matriz.append([])
        for j in range(len(a)):
            matriz[i].append(None)
    for i in range (0,len(a)):
        for j in range (0,len(a)):
             matriz[i][j] = men (a[i][j])
    return (matriz)

def mult_escal (b,a):
    matriz = []
    for i in range(len(b)):
        matriz.append([])
        for j in range(len(b)):
            matriz[i].append((0,0))
    for i in range (0,len (b)):
        for j in range (0, len (b)):
            matriz [i][j]= multi(a,(b[i][j]))
    return matriz

def transpuesta (a):
    matriz = []
    for i in range(len(a)):
        matriz.append([])
        for j in range(len(a)):
            matriz[i].append(None)
    for i in range (0,len (a)):
        for j in range (0, len (a)):
            matriz[i][j] = a[j][i]
    return (matriz)

def conjugmat (a):
    matriz = []
    for i in range(len(a)):
        matriz.append([])
        for j in range(len(a)):
            matriz[i].append(None)
    for i in range (0,len (a)):
        for j in range (0, len (a)):
            matriz[i][j] = conjug (a[i][j])
    return (matriz)

def adjunta (a):
    matriz = transpuesta(conjugmat (a))
    return (matriz)

def multimat (a,b):
    matriz = []
    for i in range(len(a)): 
        matriz.append([])
        for j in range(len(a)):
            matriz[i].append(0)
    for i in range (0,len(a)):
        for j in range (0,len(a)):
            acum =(0,0)
            for k in range (0,len(a)):
                mul = mult(a[i][k],b[k][j])
                acum = suma(acum,mul)
            matriz[i][j]= acum
    return (matriz)

def accion (a,b):
    matriz = []
    for i in range(len(b)): 
        matriz.append([])
        for j in range(1):
            matriz[i].append(0)
    for i in range (0,len(b)):
        acum =(0,0)
        for j in range (0,len(a)):
            mul = mult(b[j],a[i][j])
            acum = suma (acum,mul)
            matriz[i] = acum
    return (matriz)

def interno (a,b):
    acum=(0,0)
    for i in range (0,len(a)):
        mul = mult((conjug(a[i])),b[i])
        acum = suma (acum,mul)
    return (acum)

def norma_vect (a):
    prod = (interno(a,a))
    produ = prod [0]**0.5
    res = produ
    return (res)

def dist (a,b):
    difer = inverse (b)
    rest= addvect (a,difer)
    inte= interno (rest,rest)
    raiz = inte[0] **0.5
    res= round (raiz,2)
    return (res)

def matin(a):
    matriz = []
    for i in range(a): 
        matriz.append([])
        for j in range(a):
            matriz[i].append((0,0))
    for i in range(a):
        for j in range(a):
            if i==j:
                matriz[i][j] = (1,0)
    return matriz
def unitaria (a):
    ad = adjunta(a)
    a = multimat(a,ad)
    iden = matin(len(a))
    if a == iden:
        return True
    else:
        return False

def hermitiana (a):
    adj = adjunta (a)
    if adj == a:
        return True
    else:
        return False
def mult_ima (b,a):
    matriz = []
    for i in range(len(b)):
        matriz.append([])
        for j in range(len(b)):
            matriz[i].append(None)
    for i in range (0,len (b)):
        for j in range (0, len (b)):
            matriz [i][j]= (mult(a,(b[i][j])))
    return (matriz)

def tensor(a,b):
    resultado = []
    control = 0
    i = 0
    j = 0

    while (i < (len(a)-1)*2):
        fila = a[i]
        columna = b[j]
        res = []
        for k in fila:
            for l in columna:
                res=res + [mult(k,l)]
        j = j + 1
        columna = b[j]
        resultado= resultado + [res]
        res = []
        for k in fila:
            for l in columna:
                res=res + [mult(k,l)]
        i = i + 1
        j = j - 1
        resultado=resultado+[res]
    return (resultado)


