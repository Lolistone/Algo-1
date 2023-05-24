# Ejercicio 1.1

def perteneceFor (l: list([int]), e: int) -> bool:
    res: bool = False
    for i in range(0, len(l)):
        res = (l[i] == e) or res
    return res

def perteneceWhile (l: list([int]), e: int):
    res: bool = False
    i = 0
    while i < len(l):
        res = (l[i] == e) or res
        i += 1
    return res

def pertenece (l: list, e) -> bool:
    res: bool = False
    for i in range(0, len(l)):
        res = (l[i] == e) or res
    return res

# Ejercicio 1.2 

def divideATodosFor (l: list([int]), e: int) -> bool:
    res: bool = True
    for i in range(0, len(l)):
        res = (l[i]%e == 0) and res
    return res

def divideATodosWhile (l: list([int]), e: int) -> bool:
    res: bool = True
    i: int = 0
    while (i < len(l)):
        res = (l[i]%e == 0) and res
        i += 1
    return res

# Ejercicio 1.3

def sumaTotalFor (l: list([int])) -> int:
    suma: int = 0
    for i in range (0, len(l)):
        suma += l[i]
    return suma 

def sumaTotalWhile (l: list([int])) -> int:
    suma: int = 0
    i: int = 0
    while (i < len(l)):
        suma += l[i]
        i += 1
    return suma

# Ejercicio 1.4

def ordenadosFor (l: list([int])) -> bool:
    res: bool = True
    for i in range (0, len(l)-1):
        res = (l[i] < l[i+1]) and res
    return res

def ordenadosWhile (l: list([int])) -> bool:
    res: bool = True
    i: int = 0
    while (i < len(l)-1):
        res = (l[i] < l[i+1]) and res
        i += 1
    return res

# Ejercicio 1.5

def palabrotaFor (l: list([str])) -> bool:
    res: bool = False
    for i in range (0, len(l)):
        res = (len(l[i]) > 7) or res
    return res

def palabrotaFor2 (l: list([str])) -> bool:
    res: bool = False
    for palabra in l:
        res = (len(palabra) > 7) or res
    return res

def palabrotaWhile (l: list([str])) -> bool:
    res: bool = False
    i: int = 0
    while i < len(l):
        res = (len(l[i]) > 7) or res
        i += 1
    return res

# Ejercicio 1.6

def esPalindroma (palabra: str) -> bool:
    res: bool = True
    length: int = len(palabra)
    for i in range (0, length):
        res = (palabra[i] == palabra[length-1-i]) and res
    return res

# Ejercicio 1.7

def fortaleza (contraseña: str) -> str:
    res: str = "Amarillo"
    longitud: int = len(contraseña)
    if (longitud >= 8) and hayDigito(contraseña) and hayMayuscula(contraseña) and hayMinuscula(contraseña):
        res = "Verde"
    elif longitud <= 5:
        res = "Rojo"
    return res

# Funciones Aux

def hayDigito (contraseña: str) -> str:
    res: bool = False
    for letra in contraseña:
        res = ("0"<= letra <="9") or res
    return res 

def hayMinuscula (contraseña: str) -> bool:
    res: bool = False
    for letra in contraseña:
        res = ("a"<= letra <="z") or res
    return res

def hayMayuscula (contraseña: str) -> bool:
    res: bool = False
    for letra in contraseña:
        res = ("A"<= letra <="Z") or res
    return res

# Ejercicio 1.8

def balance (movimientos: list([tuple([str, int])])) -> int:
    saldo: int = 0
    for movimiento in movimientos:
        if movimiento[0] == "I":
            saldo += movimiento[1]
        else:
            saldo -= movimiento[1]
    return saldo
 
# Ejercicio 1.9

def vocales (palabra: str) -> bool:
    vocales: list = []
    for letra in palabra:
        if esVocal(letra) and (not pertenece(vocales, [letra])):
            vocales += [letra]
    res: bool = len(vocales) >= 3
    return res

def esVocal (letra: str) -> bool:
    res: bool = pertenece ("aeiou", letra)
    return res

# Ejercicio 2.1

