from math import *

# Ejercicio 1.1
def raizDe2() -> float:
    res: float = round(sqrt(2), 2)
    return res

# Ejercicio 1.2
def hola():
    print("hola")

# Ejercicio 1.3
def imprimir_un_verso():
    res: str = 'Tan pronto yo te vi \nNo pude descubrir'
    print(res)

# Ejercicio 1.4
def factorial2() -> float:
    res : float = 2
    return res

# Ejercicio 1.5
def factorial3() -> float:
    res : float = 3*factorial2()
    return res

# Ejercicio 1.6
def factorial4() -> float:
    res : float = 4*factorial3 ()
    return res

# Ejercicio 1.7
def factorial5() -> float:
    res : float - 5*factorial4()   
    return res

# Ejercicio 2.1
def imprimir_saludo (nombre: str):
    print ("Hola ", nombre)

# Ejercicio 2.2
def raiz_cuadrada_de (numero: int) -> float:
    res: float = sqrt(numero)
    return res

# Ejercicio 2.3
def imprimir_dos_veces (estribillo: str):
    res: str = 2* (estribillo + "\n" )
    print (res)

# Ejercicio 2.4
def es_multiplo_de (n: int, m: int) -> bool:
    res: bool = (n % m == 0)
    return res

# Ejercicio 2.5
def esPar(n: int) -> bool:
    res: bool = es_multiplo_de(n, 2)
    return res

# Ejercicio 2.6
def cant_pizzas (comensales: int, min_cantidad: int) -> int:
    porciones_min: int = (comensales * min_cantidad)
    res: int = ceil (porciones_min / 8)
    return res

# Ejercicio 3.1
def algunoEs0 (n: int, m: int) -> bool:
    res: bool = (n == 0) or (m == 0)
    return res

# Ejercicio 3.2
def ambosSon0 (n: int, m: int) -> bool:
    res: bool = (n == 0) and (m == 0)
    return res

# Ejercicio 3.3
def es_nombre_largo (nombre: str) -> bool:
    res: bool = (3 <= len (nombre) <= 8)
    return res

# Ejercicio 3.4
def esBisiesto (año: int) -> bool:
    res: bool = (es_multiplo_de(año, 4) and not(es_multiplo_de(año, 4))) or es_multiplo_de(año, 4)
    return res

# Ejercicio 4
def pesoPino (altura: int) -> int:
    alturaCM: int = altura*100
    peso: int = 0
    if alturaCM > 300:
        peso = 900 + (alturaCM - 300)*2
    else:
        peso = alturaCM*3
    return peso

def esPesoUtil (peso: int) -> bool:
    res: bool = 400 <= peso <= 1000
    return res

def sirvePino (altura: int) -> bool:
    res: bool = esPesoUtil(pesoPino(altura))
    return res

# Ejercicio 5.1
def dobleSiesPar (n: int) -> int:
    res: int = n
    if (n % 2 == 0):
        res *= 2
    return res

# Ejercicio 5.2
def devolverValorSiesPar (n: int) -> int:
    res: int = 0
    if (n % 2 == 0):
        res = n
    else:
        res = n + 1
    return res

def devolverValorSiEsPar2 (n: int ) -> int:
    res: int = 0
    if (n % 2 == 0):
        res = n
    if (n % 2 != 0):
        res = n + 1
    return res

## Ambas implementaciones funcionan (en este caso).

def devolverValorSiEsPar3 (n: int) -> int:
    res: int = n
    if (n % 2 != 0):
        res += 1
    return res

# Ejercicio 5.3

# Implementacion IfThenElseFi
def doble_triple (n: int) -> int:
    res: int = n
    if (n % 9 == 0):
        res *= 3
    elif (n % 3 == 0):
        res *= 2
    return res

# Implementacion con 2 If's. Esta implementacion falla pues python evalua todos los Ifs.
def doble_triple2 (n: int) -> int:
    res: int = n 
    if (n % 9 == 0):
        res *= 3
    if (n % 3 == 0):
        res *= 2
    return res

# Implementacion que si sirve con 2 ifs.
def doble_triple3 (n: int) -> int:
    res: int = n
    if (n % 9 == 0):
        res = n * 3
    if (n % 3 == 0 and not(n % 9 == 0)):
        res = n * 2
    return res

# Ejercicio 5.4
def tuNombre (nombre: str):
    nombreLargo: bool = 5 <= len(nombre)
    if nombreLargo:
        print("Tu nombre tiene muchas letras!")
    else:
        print("Tu nombre tiene menos de 5 caracteres")

# Ejercicio 5.5
def vacaciones (sexo: str, edad: int):
    res: str = "Anda de vacaciones"
    noJubilada: bool = (18 <= edad <= 60) and (sexo == "F")
    noJubilado: bool = (18 <= edad <= 65) and (sexo == "M")
    if noJubilado or noJubilada:
        res = "Anda a trabajar"
    return res

# Las epecificaciones estan en papel.

# Ejercicio 6

# Ejercicio 6.2
def pares ():
    i: int = 40
    while (i >= 10):
        if (i % 2) == 0:
            print(i)
        i -= 1

# Ejercicio 6.4
def despegue (n: int):
    while (n >= 1):
        print(n)
        n -= 1

# Ejercicio 6.5
def viajeEnElTiempo (partida: int, llegada: int):
    while (partida >= llegada):
        partida -= 1
        print("Viajo un año al pasado, estamos en el año", partida, "\n")

# Ejercicio 6.6
def aristoteles (año: int):
    while (año - 20) >= 384:
        año -= 20
        print("Viajo 20 años al pasado, estamos en el año", año, "\n")
 
# Ejercicio 7 (El 6 con for y saltos).
def viajeEnElTiempoFor (partida: int, llegada: int):
    partida -= 1
    llegada += 1
    for i in range (partida, llegada, -1):
        print("Viajo un año al pasado, estamos en el año", i, "\n")
    
def aristotelesFor (año: int):
    año -= 20
    for i in range (año, 383, -20):
        print("Viajo un año al pasado, estamos en el año", i, "\n")