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
def paresPorCeros (l: list[int]) -> list[int]:
    for i in range (0, len(l), 2):
        l[i] = 0
    return l

# Ejercicio 2.2
def paresPorCeros2 (l: list[int]) -> list[int]:
    res: list[int] = l
    for i in range (0, len(l), 2):
        res[i] = 0
    return res             

# Ejercicio 2.3
def sinVocales (palabra: str) -> str:
    res: str = ""
    for letra in palabra:
        if pertenece ("AEIOUaeiou", letra):
            res += ""
        else:
            res += letra
    return res

# Ejercicio 2.4
def reemplazaVocales (palabra: str) -> str:
    res: str = ""
    for letra in palabra:
        if pertenece ("aeiou", letra):
            res += "-"
        else:
            res += letra
    return res

# Ejercicio 2.5
def daVueltaStr (palabra: str) -> str:
    res: str = ""
    for i in range (len(palabra)-1, -1, -1):
        res += palabra[i]
    return res

# Ejercicio 3.1
def nombreEstudiantes() -> list[str]:
    res: list[str] = []
    nombre: str = input("Ingrese un nombre o listo: \n") 
    while (nombre != "listo"):
        res += [nombre]
        nombre = input("Ingrese un nombre o listo: \n")
    return res

# Ejercicio 3.2
def historialSUBE() -> list[tuple]:
    monedero: int = 0
    historial: list[tuple] = []
    operacion: str = input("Que operacion desea realizar? \n'C' para cargar \n'D' para descontar \n'X' para finalizar\n")
    while (operacion != "X"):
        monto: int = int(input("Ingrese el monto a ingresar/retirar: \n"))
        if (operacion == "C"):
            monedero += monto
            historial += [("C", monto)]
        elif (monto > monedero):
            print ("No posee saldo suficiente\n")
        else:
            monedero -= monto
            historial += [("D", monto)]
        operacion: str = input("Que operacion desea realizar? \n'C' para cargar \n'D' para descontar \n'X' para finalizar\n")
    return historial

import random 

# Ejercicio 3.3 .
# Como el enunciado no esclarecia cantidad de jugadores ni las reglas para ganar considere que:
# - Si el jugador suma menos de 7.5 y se para gana. 
# - Si se pasa de 7.5 pierde. 

def sieteMedio() -> list[int]:
    jugada: str = "carta"
    cartas: list[int] = []
    while (jugada != "pararse"):
        carta: int = random.choice([1,2,3,4,5,6,7,10,11,12])
        cartas += [carta]
        print("Su carta es", carta)
        if (sumaCartas(cartas) <= 7.5):
            jugada: str = input("Desea una carta o pararse?\n")
        else:
            jugada = "pararse"
            print("Has perdido!")
    if sumaCartas(cartas) <= 7.5:
        print("Has ganado!")
    return cartas

def sumaCartas(cartas: list[int]) -> float:
    res: float = 0
    for carta in cartas:
        if pertenece([10,11,12],carta):
            res += 0.5
        else:
            res += carta
    return res


# Ejercicio 4

# Ejercicio 4.1
def perteneceACadaUno (l: list[list[int]], e: int) -> list[bool]:
    res: list[bool] = []
    for lista in l:
        res += [pertenece(lista, e)]
    return res

# Ejercicio 4.2
def esMatriz (matriz: list[list[int]]) -> bool:
    cantidadFilas: int = len(matriz)
    if (cantidadFilas > 0):
        tamañoFila: int = len(matriz[0])
        res: bool = (tamañoFila > 0)
        for fila in matriz:
            res = (len(fila) == tamañoFila) and res
    return res

# Ejercicio 4.3
def filaOrdenadas (l: list[list[int]]) -> list[bool]:
    res: list[bool] = []
    for lista in l:
        res += [ordenadosFor(lista)]
    return res

# Ejercicio 4.4

# Requiere que #columnasA = #FilasB
# Mi implementaciomn utiliza randint pues trabajo con matrices en ZxZ. (Podria ampliarlo)

import numpy as np

def multiplicarMatrices (A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    cantFilas: int = len(A)
    cantColumnas: int = len(B[0])
    res: list[list[int]] = generarMatriz(cantFilas, cantColumnas)
    for i in range (0, cantFilas):
        for j in range (0, cantColumnas):
            for n in range (0, len(B)):
                res[i][j] += A[i][n]*B[n][j]
    return res

def generarMatriz(n: int, m: int) -> list[list[int]]:
    res: list[list[int]] = []
    for i in range (0, n):
        res += [[]]
        for j in range (0, m):
            res[i] += [0]
    return res

def elevarMatriz(d: int, p: int) -> list[list[int]]:
    res: list[list[int]] = np.random.randint(0, 20 + 1, (d, d)) # Genera una matriz (dxd) aleatoria con numeros entre -40 y 40.
    producto: list[list[int]] = res.copy()
    while (p > 1):
        res = multiplicarMatrices(res, producto)
        p -= 1
    return res