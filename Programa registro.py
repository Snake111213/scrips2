def agregar(e):
    x = int(input('Ingrese matricula: '))
    if x not in e:
        e = e + [x]
    else:
        print('Ya esta inscrito')
    return e 

def eliminar(e):
    x=int(input('Ingrese matricula: '))
    if x in e:
        e.remove(x)
    else:
        print('No esta inscrito')
    return e 

def consultar(e):
    x=int(input('Ingrese matricula: '))
    if x in e:
        print('Si esta inscrito')
    else:
        print('No esta inscrito')

def cubo(e):
    n = len (e)
    print('Cantidad de inscritos: ',n)

#programa principal
e = []
while True:
    print('1) Agregar registros')
    print('2) Eliminar registro')
    print('3) Consultar registros')
    print('4) Cupo actual')
    print('5) Salir')
    opc = input('Elija una opcion')

    if opc == '1':
        e = agregar(e)
    elif opc == '2':
        e = eliminar(e)
    elif opc == '3':
        consultar(e)
    elif opc == '4':
        cubo(e)
    elif opc == '5':
        print('adios')
        break
