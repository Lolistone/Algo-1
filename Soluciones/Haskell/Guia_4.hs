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

f1 :: Integer -> Integer
f1 n | n == 0 = 1
     | otherwise = (2^n) + f1 (n-1)  

f2 :: Integer -> Float -> Float
f2 n q | n == 0 = 1
       | q == 0 = 0
       | q == 1 = fromIntegral n
       | otherwise = (q ^^ n) + f2 (n-1) q

f3 :: Integer -> Float -> Float
f3 n q | n == 0 = 1
       | q == 0 = 0
       | q == 1 = fromIntegral (2*n)
       | otherwise = (q ^^ m) + f2 (m-1) q
       where m = 2*n

f4 :: Integer -> Float -> Float
f4 n q | q == 0 = 0
       | otherwise = (f3 n q) - (f2 n q) + (q^^n)

-- Ejercicio 11 --

eAprox :: Integer -> Float
eAprox n | n == 0 = 1
         | otherwise = (1 / fromInteger n) * eAprox (n-1)

e :: Float
e = eAprox 10

-- Ejercicio 12 --

sucesionAux :: Integer -> Float
sucesionAux n | n == 1 = 2
              | otherwise = 2 + (1 / sucesionAux (n-1)) 

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = (sucesionAux n) - 1

-- Ejercicio 13 --

g :: Integer -> Integer -> Integer
g i m | m == 1 = i
      | otherwise = (i ^ m) + g i (m-1)

f :: Integer -> Integer -> Integer
f n m | n == 1 = g 1 m
      | otherwise = g n m + f (n-1) m

-- Ejercicio 14 --

sumaAuxiliar :: Integer -> Integer -> Integer -> Integer
sumaAuxiliar q a b | a == 1 = q ^ (1 + b)
                   | otherwise = (q ^ (a + b)) + sumaAuxiliar q (a-1) b 

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q a b | b == 1 = sumaAuxiliar q a 1 
                    | otherwise = sumaAuxiliar q a b + sumaPotencias q a (b-1) 

-- Ejercicio 15 --

racionalesAux :: Integer -> Integer -> Float
racionalesAux p q | p == 1 = (1 / fromInteger q)
                  | otherwise = (fromInteger p/ fromInteger q) + racionalesAux (p-1) q

sumaRacionales :: Integer -> Integer -> Float
sumaRacionales p q | q == 1 = racionalesAux p 1
                   | otherwise = racionalesAux p q + sumaRacionales p (q-1)

-- Ejercicio 16 -- 

menorDivisor :: Integer -> Integer
menorDivisor n  = menorAux 2 n

menorAux :: Integer -> Integer -> Integer
menorAux k n | mod n k == 0 = k
             | otherwise = menorAux (k+1) n

--- version con listas ---

-- menorDivisor n | n == 1 = 1
--                | otherwise = head divisores
--                 where divisores = [m | m <- [2..n], mod n m == 0]

-- -- -- -- -- -- -- -- --

esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n

coPrimos :: Integer -> Integer -> Bool
coPrimos n m = (mcd n m) == 1 

mcd :: Integer -> Integer -> Integer
mcd n 0 = n
mcd n m = mcd m (mod n m)

-- nota : la funcion mcd existe y se llama gcd. (La idea de esta guia es usar recursion)

nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = encuentraPrimo 2 1 n

encuentraPrimo :: Integer -> Integer -> Integer -> Integer
encuentraPrimo p i n | i == n = p
                     | esPrimo (p+1) = encuentraPrimo (p+1) (i+1) n
                     | otherwise = encuentraPrimo (p+1) i n

-- Ejercicio 17 --

esFibonacci :: Integer -> Bool
esFibonacci n = comparoFib n 0

comparoFib :: Integer -> Integer -> Bool
comparoFib n i | fib i < n = comparoFib n (i+1)
               | fib i == n = True
               | fib i > n = False

-- Ejercicio 18 --

mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n | hayDigitoPar n = digitoPar n
                 | otherwise = -1

digitoPar :: Integer -> Integer
digitoPar n | n < 10 = n
            | esPar ultimoDigito && not (esPar anteUltDigito) = digitoPar ((div n 100)*10 + ultimoDigito)
            | not (esPar ultimoDigito) = digitoPar (div n 10)
            | ultimoDigito > anteUltDigito = digitoPar ((div n 100)*10 + ultimoDigito)
            | otherwise = digitoPar (div n 10)
            where ultimoDigito = mod n 10
                  anteUltDigito = mod (div n 10) 10
 
hayDigitoPar :: Integer -> Bool
hayDigitoPar n | n < 10 && not (esPar n) = False
               | esPar (mod n 10) = True
               | otherwise = hayDigitoPar (div n 10)

esPar :: Integer -> Bool
esPar n = mod n 2 == 0

-- Ejercicio 19 --

sumaInicialPrimos :: Integer -> Bool
sumaInicialPrimos n = existeM n n    

existeM :: Integer -> Integer -> Bool
existeM n m  | n == 2 = True
             | n == sumaPrimos m = True
             | n < sumaPrimos m = existeM n (m-1)
             | otherwise = False 

sumaPrimos :: Integer -> Integer 
sumaPrimos n | n == 1 = 2
             | otherwise = nEsimoPrimo n + sumaPrimos (n-1)

