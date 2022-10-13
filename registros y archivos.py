from pyparsing import line


while True:
    nombre = input('Ingrese el nombre del archivo: ')
    try:
        arch = open(nombre + '.txt','r')
    except FileNotFoundError:
        print('El archivo no existe')
        crear = input('Digite 1 si desea crear este archivo: ')
        if crear == '1':
            arch = open(nombre + '.txt','w')
        else:
            continue
    break

while True:
    print('\n')
    print('1) Ingresar articulo')
    print('2) Lista de articulos')
    print('3) Salir')
    opc = input('Elija una opcion: ')
    if opc =='1':
        arch = open(nombre + '.txt','a')
        cod = int(input('Ingrese codigo: '))
        cant = int(input('Ingrese la cantidad: '))
        pre = float(input('Ingrese Precio: '))
        nom = input('Ingrese nombre: ')
        linea = str(cod)+ ',' +str(cant) + ','+str(pre) + ',' + nom + '\n'
        arch.write(linea)
        arch.close()
    elif opc == '2':
        arch = open(nombre + '.txt','r')
        linea = arch.readline()
        while linea != '':
            reg = linea.split(',')
            print('Codigo: ',int(reg[0]))
            print('Cantidid: ',int(reg[1]))
            print('Precio: ',float(reg[2]))
            print('Nombre: ',reg[3])
            linea = arch.readline()

        arch.close()
    elif opc == '3':
            print('Adios')
            break

