-- Ejercicio 1 -- 

fib :: Integer -> Integer
fib n | n == 0 = 0 
      | n == 1 = 1
      | otherwise = fib (n-1) + fib (n-2)

-- Ejercicio 2 --

parteEntera :: Float -> Integer
parteEntera x | 0 <= x && x < 1 = 0
              | -1 < x && x < 0 = -1
              | x >= 1 = 1 + parteEntera (x-1)
              | x <= -1 = parteEntera (x+1) - 1

-- Ejercicio 3 --

esDivisible :: Integer -> Integer -> Bool
esDivisible n m | n == m = True
                | n < m = False 
                | otherwise = esDivisible (n-m) m

-- Ejercicio 4 --
 
sumaImapres :: Integer -> Integer
sumaImapres n | n == 1 = 1
              | otherwise = (2*n - 1) + sumaImapres (n-1)

-- Ejercicio 5 --

medioFact :: Integer -> Integer
medioFact n | n == 0 = 1 
            | n == 1 = 1
            | otherwise = n * medioFact (n-2)

-- Ejercicio 6 --

sumaDigitos :: Integer -> Integer 
sumaDigitos n | n < 10 = n
              | otherwise = (mod n 10) + sumaDigitos (div n 10)

-- Ejercicio 7 --

todosIguales :: Integer -> Bool
todosIguales n | n < 10 = True
               | n > 10 && ((mod (div n 10) 10) == mod n 10) = todosIguales (div n 10)
               | otherwise = False

-- Ejercicio 8 --

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i = mod (div n (10 ^ ((cantDigitos n) - i))) 10

cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos (div n 10)

-- Ejercicio 9 --

esCapicua :: Integer -> Bool
esCapicua n | n < 10 = True
            | n > 10 && (primerDigito == ultimoDigito) = esCapicua (sinExtremos n)
            | otherwise = False
            where primerDigito = iesimoDigito n 1
                  ultimoDigito = mod n 10
                  sinExtremos n = div (n - primerDigito*(10^((cantDigitos n)- 1))) 10 

-- Ejercicio 10 --