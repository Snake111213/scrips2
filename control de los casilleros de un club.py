'''. Diseñar una aplicación para administrar el uso de los casilleros en un club. 
Solución
En un progama se usará una matriz para representar los casilleros. Los elementos de la 
matriz contendrán el código de identificación del usuario. Un casillero libre contendra cero.
El programa incluirá la función matbuscar desarrollada anteriormente
Para la interacción se propone un menú con las siguientes opciones:
1) Asignar casillero
2) Devolver casillero
3) Consultar casillero
4) Consultar usuario
5) Salir'''

from numpy import*
def matbuscar(a,x):
    [n,m]=shape(a)
    for i in range(n):
        for j in range(m):
            if x==a[i][j]:
                return [i,j]
    return [-1,-1]

n=int(input('Cuantas filas: '))
m=int(input('Cuantas columnas: '))
c=zeros([n,m],int)

while True:
    print('1) Asignar un casillero')
    print('2) Devolver casillero')
    print('3) Consultar casillero')
    print('4) Consultar usuario')
    print('5) Salir')

    opcion = input('Elija una opcion: ')
    if opcion == '1':
        i = int(input('Cual fila: '))
        j = int(input('Ingrese el codigo: '))
        if c[i][j] == 0:
            e = int(input('Ingrese el codigo: '))
            c[i][j]==e
        else:
            print('casillero ocupado')

    elif opcion == '2':
        i = int(input('Cual fila: '))
        j = int(input('Cual columna: '))
        if c[i][j]==0:
            print('Casillero no esta asignado')
        else:
            c[i][j]=0
        
    elif opcion == '3':
        i = int(input('Cual fila: '))
        j = int(input('Cual columna: '))
        if c[i][j]==0:
            print('El casillero no asignado')
        else:
            print('El casillero esta ocupado')
    
    elif opcion == '4':
        codigo = int(input('Ingrese el codigo: '))
        [i,j] = matbuscar(c,codigo)
        if i>=0 and j>=0:
            print(f'El usuario esta en el casillero: {i,j}')
        else:
            print('El usuario no tiene casillero asignado')

    elif opcion == '5':
        print('Adios')




