from venv import create


while True:
    nombre = input('Ingrede el nombre del archivo: ')

    try:
        arch = open(nombre + '.txt','r')
    except FileNotFoundError:
        print('El archivo no existe')
        crear = input('Digite 1 si desea crear este archivo: ') 
        if crear == '1':
            arch = open(nombre + ' .txt', 'w')
        else:
            continue

    break