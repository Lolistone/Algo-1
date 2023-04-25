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

maximo :: [Integer] -> Integer
maximo [x] = x
maximo (x:xs) = max x (maximo xs)

pares :: [Int] -> [Int]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x: pares xs
             | otherwise = pares xs
