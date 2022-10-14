'''Una función generadora permite definir un dispositivo para interrumpir de manera elegante 
un ciclo doble:
Ejemplo. Suponer que se desea encontrar el primer caso en el que los valores i, j 
cumplen la condición:
 2i3 + 3j2 es divisible para 7, para i,j = 1,2,3,. . .,9
En el siguiente programa, la instrucción break solamente interrumpe las repeticiones del 
ciclo en el que se ejecuta la instrucción break, en este caso el ciclo interno:'''

for i in range(1,10):
    for j in range(1,10):
        n=2*i**3+3*j**2
        if n%7==0:
            print(i,j,n)
            break
