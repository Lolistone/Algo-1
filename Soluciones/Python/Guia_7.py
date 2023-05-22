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

# Ejercicio 2.7
def es_nombre_largo (nombre: str) -> bool:
    res: bool = (3 <= len (nombre) <= 8)
    return res

