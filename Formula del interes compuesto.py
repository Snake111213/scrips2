'''La siguiente fórmula del interés compuesto relaciona la cantidad de depósitos, el
valor mensual constante de cada depósito, y el interés pactado al invertir el dinero en una 
cuenta. Se requiere escribir un programa interactivo con un menú para su utilización
n (1 x) 1 A P
x
  + − =    
, en donde
A: Valor acumulado, 
P: Valor de cada depósito mensual
n: Cantidad de depósitos mensuales 
x: Tasa de interés mensual
Solución
Se escribirá un programa con un menú para calcular alguno de los valores de: A, P, n'''

#formula del interes compuesto
from math import*
while True:
    print('1) Valor acumulado')
    print('2) Deposito Mensual')
    print('3) Numero de depositos')
    print('4) Salir')
    opc=input('Elija una opcion: ')
    if opc=='1':
        p=float(input('Valor del deposito mensual: '))
        n=int(input('Numero de depositos mensuales: '))
        x=float(input('Interes anual en porsentaje: '))
        m=0.01*x/12
        a=p*((1+m)**n-1)/m
        print('Valor acumulado: ',a)
    elif opc=='2':
        a=float(input('Valor acumulado: '))
        n=int(input('Valor acumulado: '))
        x=float(input('Interes anual en porcenteje: '))
        m=0.01*x/12
        p=a*m/((1+m)**n-1)
        print('Cuota mensual: ',p)
    elif opc=='3':
        a=float(input('Valor acumulado: '))
        p=float(input('valor del deposito mensual: '))
        x=float(input('Interes anual en porcentaje: '))
        m=0.01*x/12
        n=log(a*m/p+1)/log(1+m)
        print('Numero de depositos: ',n)
    elif opc=='4':
        print('Adios')
        break