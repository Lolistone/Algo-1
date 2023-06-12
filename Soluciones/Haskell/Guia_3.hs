-- Ejercicio 1 -- 

f :: Int -> Int
f n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

g :: Int -> Int
g n | n == 131 = 1
    | n == 8 = 16
    | n == 16 = 4

h :: Int -> Int
h n = f (g (n))

k :: Int -> Int
k n = g (f (n))

-- Ejercicio 2 --

absoluto :: Int -> Int
absoluto n | n >= 0 = n
           | otherwise = -n

maximoAbsoluto :: Int -> Int -> Int
maximoAbsoluto x y | absoluto x > absoluto y = absoluto x
                   | otherwise = absoluto y

maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z | x >= y && x >= z = x
              | y >= x && y >= z = y
              | otherwise = z

algunoEs0 :: Float -> Float -> Bool
-- algunoEs0 x y | x == 0 || y == 0 = True
--               | otherwise = False

-- Solucion con pattern matching

algunoEs0 0 _ = True
algunoEs0 _ 0 = True
algunoEs0 x y = False

ambosSon0 :: Float -> Float -> Bool
-- ambosSon0 x y | x == 0 && y == 0 = True
--               | otherwise = False
    
-- Solucion con pattern matching

ambosSon0 0 0 = True
ambosSon0 x y = False

mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y | x <= 3 && y <= 3 = True
                   | (x > 3 && x <= 7) && (y > 3 && y <= 7) = True
                   | x > 7 && y > 7 = True
                   | otherwise = False

sumaSinRepetidos :: Int -> Int -> Int -> Int
sumaSinRepetidos x y z | x == y && y == z = x
                       | x == y && y /= z = y + z
                       | x /= y && (y == z || x == z) = x + y
                       | otherwise = x + y + z 

esMultiplode :: Int -> Int -> Bool
esMultiplode n m | mod n m == 0 = True
                 | otherwise = False 

digitoUnidades :: Int -> Int
digitoUnidades n = mod n 10

digitoDecenas :: Int -> Int
digitoDecenas n = div (mod n 100) 10

-- Ejercicio 3 --

estanRelacionados :: Int -> Int -> Bool
estanRelacionados a b | mod (-a) b == 0 = True
                      | otherwise = False

-- Ejercicio 4 --

prodInterno :: (Float, Float) -> (Float, Float) -> Float
prodInterno (vx, vy) (wx, wy) = vx*wx + vy*wy

todoMenor :: (Float, Float) -> (Float, Float) -> Bool
todoMenor  (vx, vy) (wx, wy) | vx < wx && vy < wy = True
                             | otherwise = False

distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (vx, vy) (wx, wy) = sqrt(((vx-wx)**2)+((vy-wy)**2))

sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (x, y, z) = x + y + z

sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (x, y, z) n = multiplo x n + multiplo y n + multiplo z n
                                 where multiplo x n | mod x n == 0 = x
                                                    | otherwise = 0

posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (x, y, z) | esPar x = 1
                       | esPar y = 2
                       | esPar z = 3
                       | otherwise = 4
                       where esPar n | mod n 2 == 0 = True
                                     | otherwise = False

crearPar :: a -> b -> (a, b)
crearPar a b = (a, b)

invertir :: (a, b) -> (b, a)
invertir (a, b) = (b, a)

-- Ejercicio 5 --

todosMenores :: (Int, Int, Int) -> Bool
todosMenores (x, y, z) | (f1 x > g1 x) && (f1 y > g1 y) && (f1 z > g1 z) = True
                       | otherwise = False 

f1 :: Int -> Int
f1 n | n <= 7 = n ^ 2
     | otherwise = 2*n - 1

g1 :: Int -> Int
g1 n | esPar n = div n 2
     | otherwise = 3*n + 1
     where esPar n | mod n 2 == 0 = True
                   | otherwise = False

-- Ejercicio 6 -- 

bisiesto :: Int -> Bool
bisiesto year | not (esMultiplode year 4) || (esMultiplode year 100 && not (esMultiplode year 400)) = False
              | otherwise = True

-- Ejercicio 7 --

distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (vx, vy, vz) (wx, wy, wz) = abs (vx - wx) + abs (vy - wy) + abs (vz - wz)

-- Ejercicio 8 --

comparar :: Int -> Int -> Int
comparar a b | sumaUltimosDosdigitos(a) < sumaUltimosDosdigitos (b) = 1
             | sumaUltimosDosdigitos(a) > sumaUltimosDosdigitos (b) = -1
             | otherwise = 0
             where sumaUltimosDosdigitos n = digitoUnidades n + digitoDecenas n