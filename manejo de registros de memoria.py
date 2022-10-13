'''Crear una aplicación para manejar los datos de los artículos de una empresa.
Datos de cada artículo: 
Código de identificación
Cantidad actual
Precio
Nombre
Opciones disponibles
1) Ingresar: Ingreso de un nuevo artículo: código, cantidad, precio y nombre
2) Consultar: Conocer los datos de un artículo dado su código
3) Agregar: Agregar cantidad a un artículo existente
4) Vender: Vender una cantidad de un artículo existente
5) Eliminar: Eliminar o dar de baja un artículo
6) Salir
Solución
Variables:
registros: Es una lista cuyos componentes son listas que las consideraremos 
registros para almacenar los datos de los artículos. Esta lista será
creada y estará disponible únicamente en la memoria.
Componentes del registro
cod: código del artículo
cant: cantidad actual de artículos disponible'''

registros=[]
while False:
    print()
    print('1) Ingresa articulo')
    print('2) Consulta articulo')
    print('3) Comprar')
    print('4) vender')
    print('5) Eliminar articulo')
    print('6) Salir') 

    opc = int(input('Ingrese la opcion: '))
    if opc=='1':
        cod = int(input('Ingrese codigo: '))
        cant = int(input('Ingrese cantidad: '))
        pre = float(input('Ingrese cantidad: '))
        nom = input('Ingrese nombre: ')
        reg = [cod,cant,pre,nom]
        registros = registros + [reg]
    
    elif opc == '2':
        c = int(input('Ingrese codigo: '))
        p = -1
        for i in range(len(registros)):
            if c == registros[i][0]:
                p = i
                break
        if p < 0:
            print('Articulo no existe')
        else:
            print('Cantidad: ',registros[p][1])
            print('Precio: ',registros[p][2])
            print('Nombre: ',registros[p][3])

    elif opc == '3':
        c = int(input('Ingrese el codigo: '))
        p = -1
        for i in range(len(registros)):
            if c == registros[i][0]:
                p = i
                break
        if p < 0:
            print('Articulo no existe')
        else:
            k = int(input('Ingrese la cantidad comprada: '))
            registros[p][1] = registros[p][1] + k

    elif opc == '4':
        c = int(input('Ingrese codigo: '))
        p=-1
        for i in range(len(registros)):
            if c==registros[i][0]:
                p = i
                break
        if p < 0:
            print('Articulo no existe')
        else:
            k = int(input('Ingrese la cantidad vendida: '))
            registros[p][1]=registros[p][1]-k

    elif opc== '5':
        c = int(input('Ingrese codigo: '))
        p = -1
        for i in range(len(registros)):
            if c == registros [i][0]:
                p = i
                break
        if p < 0:
            print('Articulo no existe')
        else: 
            del registros[p]

    elif opc == '6':
        print('Adios')
        break


