-- Ejercicio 1 --

longitud :: [t] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

ultimo :: [t] -> t
ultimo (x:xs) | (longitud xs == 0) = x
              | otherwise = ultimo xs

principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x: principio xs

reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = (reverso xs) ++ [x]

-- Ejercicio 2 --

pertenece :: (Eq t) => [t] -> t -> Bool
pertenece [] _ = False
pertenece (x:xs) e | x == e = True
                   | otherwise = pertenece xs e 

todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [_] = True
todosIguales (x:xs) | x == (head xs) = todosIguales xs
                    | otherwise = False

todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos (x:xs) | pertenece xs x = False
                      | otherwise = todosDistintos xs

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | pertenece xs x = True
                      | otherwise = hayRepetidos xs

quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar y (x:xs) | x == y = xs
                | otherwise = x: quitar y xs

quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos y (x:xs) | x == y && pertenece xs y = quitarTodos y xs
                     | x == y = xs
                     | otherwise = x: quitarTodos y xs

eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) | pertenece xs x = x: eliminarRepetidos (quitarTodos x xs)
                         | otherwise = x: eliminarRepetidos xs

mismosElementos ::  (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos s r = listaContenida s r && listaContenida r s

-- Funcion Auxiliar para mismosElementos. -- 

listaContenida :: (Eq t) => [t] -> [t] -> Bool
listaContenida [] _ = True
listaContenida (x:xs) lista | pertenece lista x = listaContenida xs lista
                            | otherwise = False

-- -- -- -- -- -- -- -- -- -- -- -- -- -- --

capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua [_] = True
capicua (x:xs) | x == ultimo xs = capicua (principio xs)
               | otherwise = False

-- Ejercicio 3 -- 

sumatoria :: [Integer] -> Integer
sumatoria [x] = x
sumatoria (x:xs) = x + sumatoria xs

productoria :: [Integer] -> Integer
productoria [x] = x
productoria (x:xs) = x * (productoria xs)
 
maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs) = max x (maximo xs)

sumarN :: Integer -> [Integer] -> [Integer]
sumarN _ [] = []
sumarN n (x:xs) = (n+x): (sumarN n xs)

sumarElPrimero :: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo (x:xs) = sumarN (ultimo xs) (x:xs)

pares :: [Int] -> [Int]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x: pares xs
             | otherwise = pares xs

multiplosDeN :: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | x `mod` n == 0 = x: (multiplosDeN n xs)
                      | otherwise = multiplosDeN n xs

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar (x:xs) = ordenar (quitar (maximo (x:xs)) (x:xs)) ++ [maximo (x:xs)]

-- Ejercicio 4 --

sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos (x:xs) | x == ' ' && (head xs) == ' ' = sacarBlancosRepetidos xs
                             | otherwise = x: (sacarBlancosRepetidos xs)

contarPalabras :: [Char] -> Integer
contarPalabras [] = 0
contarPalabras [_] = 1
contarPalabras (x:xs) | x == ' ' = 1 + contarPalabras xs
                      | otherwise = contarPalabras xs

palabraMasLarga :: [Char] -> [Char]
palabraMasLarga l = palabraMasLargaAux (palabras l)

-- Defino funciones auxiliares para palabraMasLarga ---

palabraMasLargaAux :: [[Char]] -> [Char]
palabraMasLargaAux [x] = x
palabraMasLargaAux (x:xs) | longitud x == maximo (longitudes (x:xs)) = x
                          | otherwise = palabraMasLargaAux xs

longitudes :: [[Char]] -> [Integer]
longitudes [x] = [longitud x] 
longitudes (x:xs) = (longitud x): longitudes xs 

--- --- --- --- --- --- --- --- --- --- --- --- --- --- 

palabras :: [Char] -> [[Char]]
palabras [] = [""]
palabras (x:xs) | x == ' ' = "": rest
                | otherwise = (x: head rest) : tail rest
                where rest = palabras xs

aplanar :: [[Char]] -> [Char]
aplanar [] = ""
aplanar (x:xs) = x ++ (aplanar xs)

aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = ""
aplanarConBlancos [x] = x
aplanarConBlancos (x:xs) = x ++ [' '] ++ (aplanarConBlancos xs)

aplanarConNBlancos :: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _ = ""
aplanarConNBlancos [x] _ = x
aplanarConNBlancos (x:xs) n = x ++ (generarNblancos n) ++ (aplanarConNBlancos xs n)

-- Funcion auxiliar para aplanarConNBlancos -- 

generarNblancos :: Integer -> [Char]
generarNblancos 0 = []
generarNblancos n = [' '] ++ generarNblancos (n-1)

-- Ejercicio 5 --

nat2bin :: Integer -> [Integer]
nat2bin 0 = [0]
nat2bin 1 = [1]
nat2bin n = (nat2bin (div n 2)) ++ [mod n 2]

bin2nat :: [Integer] -> Integer
bin2nat [0] = 0
bin2nat [1] = 1
bin2nat (x:xs) = x * (2 ^ (longitud (x:xs) - 1)) + bin2nat xs

nat2hex :: Integer -> [Char]
nat2hex n | n < 10 = show n
          | n == 10 = ['A']
          | n == 11 = ['B']
          | n == 12 = ['C']
          | n == 13 = ['D']
          | n == 14 = ['E']
          | n == 15 = ['F']
          | otherwise = nat2hex (div n 16) ++ nat2hex (mod n 16)

sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [x] = [x]
sumaAcumulada (x:xs) = x: sumaAcumulada ((x + head xs): tail xs)

descomponerEnPrimos :: [Integer] -> [[Integer]]
descomponerEnPrimos [x] = [primosAux x 2]
descomponerEnPrimos (x:xs) = (primosAux x 2): descomponerEnPrimos xs

-- Funcion auxiliar para descomponerEnPrimos

primosAux :: Integer -> Integer -> [Integer]
primosAux 1 _ = []
primosAux 2 _ = [2]
primosAux n i | mod n i == 0 = i: primosAux (div n i) i
              | otherwise = primosAux n (i+1) 

-- Ejercicio 6 --

type Set a = [a]

-- En todas las funciones asumo que estoy ingresando conjuntos validos, es decir sin repetidos --

agregarATodos :: Integer -> Set (Set Integer) -> Set (Set Integer)
agregarATodos n [] = []
agregarATodos n (x:xs) = (n: x): agregarATodos n xs

partes :: Integer -> Set (Set Integer)
partes 0 = partesAux []
partes n = partesAux [1..n]

-- Defino una funcion auxiliar para partes -- 

-- Usando agregarTodos (Que es como se espera que se haga) --

partesAg :: Set Integer -> Set (Set Integer)
partesAg [] = [[]]
partesAg (x:xs) = agregarATodos x (partesAux xs) ++ partesAux xs

-- Usando map --

partesAux :: Set Integer -> Set (Set Integer)
partesAux [] = [[]]
partesAux (x:xs) = map (x:) (partesAux xs) ++ partesAux xs

-- Con listas por comprension --

partesComp :: Set Integer -> Set (Set Integer)
partesComp [] = [[]]
partesComp (x:xs) = [x:e | e <- partesAux xs] ++ partesAux xs

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

productoCartesiano :: Set Integer -> Set Integer -> Set (Integer, Integer)
productoCartesiano [] _ = []
productoCartesiano _ [] = []
productoCartesiano (x:xs) (y:ys) = cartesianoAuxiliar (x:xs) y ++ productoCartesiano (x:xs) ys

cartesianoAuxiliar :: Set Integer -> Integer -> Set (Integer, Integer)
cartesianoAuxiliar [] _ = []
cartesianoAuxiliar [1] n = [(1,n)]
cartesianoAuxiliar (x:xs) n = (x,n): cartesianoAuxiliar xs n