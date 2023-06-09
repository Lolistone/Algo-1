# Archivos

# Ejercicio 1.1
def contarLineas (nombreArchivo: str) -> int:
    f = open(nombreArchivo, 'r')
    finArchivo: bool = False
    res: int = 0
    while not finArchivo:
        finArchivo = f.readline() == ''
        if not finArchivo:
            res += 1
    f.close()
    return res

def contarLineas2 (nombreArchivo: str) -> int:
    f = open(nombreArchivo, 'r')
    lineas: list[int] = f.readlines()
    f.close()
    res: int = len(lineas)
    return res

# Ejercicio 1.2
def existePalabra (palabra: str, nombreArchivo: str) -> bool:
    f = open(nombreArchivo, 'r')
    res: bool = False
    for i in range (0, contarLineas(nombreArchivo)):
        linea: list[str] = (f.readline()).split()
        res = res or (palabra in linea)
    f.close()
    return res

# Ejercicio 1.3
def cantidadDeApariciones (palabraBuscada: str, nombreArchivo: str) -> bool:
    f = open(nombreArchivo, 'r')
    res: int = 0
    for i in range (0, contarLineas(nombreArchivo)):
        linea: list[str] = (f.readline()).split()
        for palabra in linea:
            if palabra  == palabraBuscada:
                res += 1
    return res

#msorondo@live.com.ar

# Ejercicio 2
def clonarSinComentarios(nombreArchivo: str):
    archivoAclonar = open(nombreArchivo, 'r')
    clon = open('clon' + nombreArchivo, 'w')
    finArchivo: int = False
    while not finArchivo:
        linea: str = archivoAclonar.readline()
        lineaDivida: list[str] = linea.split('#')
        if '\n' in lineaDivida[0]:
            clon.write(lineaDivida[0])
        else:
            clon.write(lineaDivida[0] + '\n')
        finArchivo = finArchivo or linea == ''
    archivoAclonar.close()
    clon.close()

# Ejercicio 3
def reverso(nombreArchivo: str):
    archivo = open(nombreArchivo, 'r')
    nuevoArchivo = open('reverso.txt', 'w')
    lineas: list[str] = archivo.readlines()
    for i in range (len(lineas)-1, -1, -1):
        nuevoArchivo.write(lineas[i])
    archivo.close()
    nuevoArchivo.close()

# Ejercicio 4
def fraseFinal(nombreArchivo: str, frase: str):
    archivo = open(nombreArchivo, 'r')
    lineas: list[str] = archivo.readlines()
    lineas.append(frase)
    archivo.close()
    archivo = open(nombreArchivo, 'w')
    for linea in lineas:
        if '\n' in linea:
            archivo.write(linea)
        else:
            archivo.write(linea + '\n')
    archivo.close()

# Ejercicio 5
def frasePrincipio(nombreArchivo: str, frase: str):
    archivo = open(nombreArchivo, 'r')
    lineas: list[str] = [frase]
    lineas += archivo.readlines()
    archivo.close()
    archivo = open(nombreArchivo, 'w')
    for linea in lineas:
        if '\n' in linea:
            archivo.write(linea)
        else:
            archivo.write(linea + '\n')
    archivo.close()

# Ejercicio 6
def palabrasLegibles(nombreArchivo: str):
    archivo = open(nombreArchivo, 'rb')
    finArchivo: bool = False
    palabras: list[str] = []
    while (not finArchivo):
        linea: str = archivo.readline()
        palabra: str = ''
        for i in range(0, len(linea)):
            if ('A' <= chr(linea[i]) <= 'Z') or ('a' <= chr(linea[i]) <= 'z') or (chr(linea[i]) == '_') or (chr(linea[i]) == ' ') or ('0' <= chr(linea[i]) <= '9'):
                palabra += chr(linea[i])
            else:
                palabras += [palabra]
                palabra = ''
        finArchivo: bool = linea == b''
    i: int = 0
    while (i < len(palabras)):
        if len(palabras[i]) < 5:
            palabras.remove(palabras[i])
            i -= 1
        i+=1
    archivo.close()
    return palabras

# Ejercicio 7
def promedioEstudiante (lu: str) -> float:
    f = open('notas.csv', 'r')
    i: int = 0
    sumaNotas: int = 0
    cantNotas: int = 0
    while (i < contarLineas('notas.csv')):
        alumno: list[str] = (f.readline()).split(', ')
        if alumno[0] == lu:
            sumaNotas += float(alumno[3])
            cantNotas += 1
        i += 1
    f.close()
    promedio: int = sumaNotas / cantNotas
    return promedio

# Pilas
from queue import LifoQueue as Pila
import random

# Ejercicio 8
def generarNumerosAlAzar (n: int, desde: int, hasta: int) -> list[int]:
    myList: list[int] = []
    for i in range(desde, hasta+1):
        myList += [i]
    res: list[int] = random.sample(myList, n)
    return res

# Ejercicio 9
def pilaAleatoria(n: int, desde: int, hasta: int) -> Pila:
    p = Pila()
    numerosAlAzar = generarNumerosAlAzar(n,desde,hasta)
    for i in range (0, n):
        p.put(numerosAlAzar[i])
    return p

# Ejercicio 10
def cantidadDeElmentos(p: Pila) -> int:
    res: int = 0
    while not(p.empty()):
        p.get()
        res += 1
    return res

# Ejercicio 11
def buscarElMaximo(p: Pila) -> int:
    res: int = p.get()
    while not(p.empty()):
        next: int = p.get()
        if (res < next):
            res = next
    return res

# Ejercicio 12
def estaBienBalanceada(s: str)  -> bool:
    parentesis: Pila = Pila()
    operaciones: list[str] = ['+', '-', '/', 'x']
    res: bool = True
    for i in range (0, len(s)):
        if s[i] == '(':
            if i > 0 and not(('0' <= s[i-1] <= '9') or ('0' <= s[i-2] <= '9')):
                parentesis.put('(')
            elif i == 0: 
                parentesis.put('(')
            else: 
                res = False
        elif s[i] == ')':
            if parentesis.empty() or s[i-1] == '(':
                res = False
            elif not(s[i-1] in operaciones):
                if s[i-2] == '(' and s[i-1] == ' ':
                    res = False
                else:
                    parentesis.get()
    res = res and parentesis.empty()
    return res
 
# Colas
from queue import Queue as Cola

# Ejercicio 13
def colaAleatoria(n: int, desde: int, hasta: int) -> Cola:
    c = Cola()
    listaAletoria: list[int] = generarNumerosAlAzar(n, desde, hasta)
    for number in listaAletoria:
        c.put(number)
    return c

# Ejercicio 14.
def cantidadElementosCola(c: Cola) -> int:
    res: int = 0
    while not(c.empty()):
        c.get()
        res += 1
    return res

# Ejercicio 15
def buscarElMaximoCola(c: Cola) -> int:
    res: int = c.get()
    while not(c.empty()):
        next: int = c.get()
        if (res < next):
            res = next
    return res

# (Notar que las implementaciones de los ejercicio 14, 15 son identicas a las de Pila)

# Ejercicio 16
def armarSecuenciaBingo() -> Cola[int]:
    res: Cola[int] = colaAleatoria(100, 0, 99)
    return res

def jugarCartonDeBingo(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas: int = 0
    jugada: int
    bingo: bool = False
    while not(bingo):
        jugada = bolillero.get()
        if jugada in carton:
            carton.remove(jugada)
        jugadas += 1
        bingo = len(carton) == 0
    return jugadas

# Ejercicio 17
def nPacientesUrgentes(c: Cola[(int, str, str)]) -> int:
    res: int = 0
    paciente: tuple(int, str, str)
    while not(c.empty()):
        paciente = c.get()
        if paciente[0] <= 3:
            res += 1
    return res

# Diccionarios 

# Ejercicio 18
def agruparPorLongitud(nombreArchivo : str) -> dict:
    archivo = open(nombreArchivo, 'r')
    tamañoArchivo: int = contarLineas(nombreArchivo)
    res: dict = {}
    for k in range(0, tamañoArchivo):
        linea: list[str] = (archivo.readline()).split()
        for palabra in linea:
            if len(palabra) in res.keys():
                res[len(palabra)] = res[len(palabra)] + 1
            else:
                res[len(palabra)] = 1
    return res

# Ejercicio 19
def promedio() -> int:
    f = open('notas.csv', 'r')
    i: int = 0
    promedios: dict = {}
    while (i < contarLineas('notas.csv')):
        alumno: list[str] = (f.readline()).split(', ')
        if not(alumno[0] in promedios.keys()):
            promedios[alumno[0]] = promedioEstudiante(alumno[0]) 
        i += 1
    f.close()
    return promedios

# Ejercicio 20 (Considero palabras a secuencias de caracteres sin espacios)
def apariciones(nombreArchivo: str) -> dict:
    archivo = open(nombreArchivo, 'r')
    apariciones: dict = {}
    i: int = 0
    while (i < contarLineas(nombreArchivo)):
        linea: list[str] = (archivo.readline()).split(' ')
        for palabra in linea:
            if not(palabra in apariciones.keys()):
                apariciones[palabra] = cantidadDeApariciones(palabra, nombreArchivo)
        i += 1
    archivo.close()
    return apariciones

def palabraFrecuente(nombreArchivo: str) -> str:
    cantApar: dict = apariciones(nombreArchivo)
    claves: list[str] = list(cantApar.keys())
    res: str = claves[0]
    for clave in claves:
        if cantApar[res] <= cantApar[clave]:
            res = clave
    return res