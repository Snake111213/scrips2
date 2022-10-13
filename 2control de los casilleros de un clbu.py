from numpy import*
def matbuscar(a,x):
    [n,m]=shape(a)
    for i in range(n):
        for j in range(m):
            if x==a[i][j]:
                return [i,j]
    return [-1, -1]

def asignar(c):
    i = int(input('Cual fila: '))
    j = int(input('Cual columna: '))
    if c[i][j]==0:
        e = int(input('Ingrese el codigo: '))
        c[i][j]=e
    else:
        print('Casillero ocupado')
    return c

def devolver(c):
    i = int(input('Cual fila: '))
    j = int(input('Cual columna: '))
    if c[i][j]==0:
        print('Casillero no esta asigado')
    else:
        c[i][j]=0
    return c

def casillero(c):
    i = int(input('Cual fila: '))
    j = int('cual columna: ')
    if c[i][j]==0:
        print('Casillero no esta ocupado')
    else:
        print('El casillero esta ocupado')

def usuario(c):
    x = int('Ingrese el codigo: ')
    [i,j]=matbuscar(c,x)
    if i>=0 and j>=0:
        print('El usuario esta en el casillero: ', i,j)
    else:
        print('El usuario no tiene casillero asignado')

n = int(input('Cuantas filas: '))
m = int(input('Cuantas columnas: '))
c=zeros([n,m],int)

while True:
    print('1) Asignar un casillero')
    print('2) Devolver casillero')
    print('3) Consultar usuario')
    print('4) consultar usuario')
    print('5) Salir')

    respuesta = (input('Elija una opcion: '))
    if respuesta == '1':
        c=asignar(c)
    elif respuesta == '2':
        c=devolver(c)
    elif respuesta == '3':
        c=casillero(c)
    elif respuesta == '4':
        c=usuario(c)
    elif respuesta == '5':
        print('Adios')
        break