from multiprocessing.sharedctypes import Value
from numpy import intp
from pyparsing import line


def apertura():
    global archivo
    while True:
        archivo = input('Ingrese el nombre del archivo: ')
        try:
            arch = open(archivo + '.txt','r')
            arch.close()
        except FileNotFoundError:
            print('El archivo no existe')
            crear = input('Digite 1 si desea crear este archivo: ')
            if crear == '1':
                arch = open(archivo + '.txt','w')
                arch.close()
            else:
                continue
        return

def ingreso():
    global archivo
    try:
        c = int(input('Ingrese codigo: '))
    except ValueError:
        print('Codigo incorrecto')
        return
    if c <= 0:
        print('Codigo incorrecto')
        return
    [exito,pos]=buscar_registro(c)
    if exito:
        print('Codigo ya existe')
    else:
        try:
            cant = int(input('Ingrese cantidad: '))
            pre = int(input('ingrese precio: '))
            nom = input('Ingrese nombre: ')
        except ValueError:
            print('Dato incorrecto')
            return
        linea = str(c).rjust(5) + ',' + str(cant).rjust(6) + ',' + str(pre).rjust(8) + ',' +nom.rjust(20)

        grabar_registro(linea)

def consulta():
    global archivo
    try:
        c = int(input('Ingrese codigo: '))
    except ValueError:
        print('codigo incorrecto')
        return
    [exito,pos] = buscar_registro(c)
    if exito:
        linea = leer_registro(pos)
        [cod,cant,pre,nom] = linea_a_registro(linea)
        print('Codigo: ',cod)
        print('Cantidad: ',cant)
        print('Precio: ',pre)
        print('Nombre: ',nom.strip())
    else:
        print('Registro no existe')

def comprar():
    global archivo
    try:
        c = int(input('Ingrese codigo: '))
    except ValueError:
        print('Codigo incorrecto')
        return
    [exito,pos] = buscar_registro(c)
    if exito:
        try:
            k = int(input('Ingrese la cantidad comprada: '))
        except ValueError:
            print('Dato incorrecto')
            return
        reemplaza_registro(pos,k)
    else:
        print('Registro no existe')

def vender():
    global archivo
    try:
        c = int(input('Ingrese codigo: '))
    except ValueError:
        print('Codigo incorrecto')
        return
    [exito,pos] = buscar_registro(c)
    if exito:
        linea = leer_registros(pos)
        [cod,cant,pre,nom] = linea_a_registro(linea)
        try:
            k = int(input('Ingrese la cantidad vendida'))
        except ValueError:
            print('Dato incorrecto')
            return
        if K > cant:
            print('Cantidad disponoble')
            return
        
         reemplaza_registros(pos,-k)
    else:
        print('Registro no existe')

def eliminar():
    global archivo
    try:
        c = int(input('Ingrese codigo: '))
    except ValueError:
        print('Codigo incorrecto')
        return
    [exito,pos] = buscar_registro(c)
    if exito:
        encera_registro(pos)
    else:
        print('Registro no existe')

def leer_registro(pos):
    global archivo
    arch = open(archivo + '.txt','r')
    arch.seek(pos)
    linea = arch.readline()
    return linea

def buscar_registro(c):
    global archivo
    arch = open(archivo + '.txt','r')
    pos = arch.tell()
    linea = arch.readline()
    exito = False
    while linea != '': 
        [cod,cant,pre,nom] = linea_a_registro(linea)
        if c == cod:
            exito = True
            break
        pos = arch.readline()
        linea = arch.readline()
    arch.close()
    return [exito, pos]


def grabar_registro(linea):
    global archivo
    [exito, pos] = buscar_bloque_libre()
    if exito:
        arch = open(archivo + '.txt','r')
        arch.seek(pos)
        arch.write(linea)
        arch.close()
    else:
        arch = open(archivo + '.txt','a')
        arch.write(linea)
        arch.close()

def buscar_bloque_libre():
    global archivo
    arch = open(archivo + '.txt','r')
    pos = arch.tell()
    linea = arch.readline()
    exito = False
    while linea != '':
        [cod,cant,pre,nom] = linea_a_registro(linea)
        if cod == 0:
            exito = True
            break
        pos = arch.tell()
        linea = arch.readline()
    arch.close()
    return [exito, pos]

def encera_registro(pos):
    global archivo
    linea = leer_registro(pos)
    [cod,cant,pre,nom] = linea_a_registros(linea)
    cod = 0
    linea = str(c) .rjust(5)+','+str(cant).rjust(6)+ ','+str(pre).rjust(8)+','+nom.rjust(20)+ '\n'

    arch = open(archivo + '.txt', 'r+')
    arch.seek(pos)
    arch.seek(pos)
    arch.write(linea)
    arch.close()

def linea_a_registro(linea):
    x = linea.split(',')
    cod = int(x[0])
    cant = int(x[1])
    pre = float(x[2])
    nom=x[3[0:len(x[3])-1]]
    return [cod,cant,[pre,nom]]

apertura()
while True:
    print('')
    print('1) Ingresar articulo')
    print('2) Consultar articulo')
    print('3) Comprar')
    print('5) Eliminar')
    print('6) Salir')
    opc = input('Elija una opcion: ')
    if opc=='1':
        ingreso()
    elif opc=='2':
        consulta()
    elif opc=='3':
        comprar()
    elif opc=='4':
        vender()
    elif opc=='5':
        eliminar()
    elif opc=='6':
        print('Adios')
        break

