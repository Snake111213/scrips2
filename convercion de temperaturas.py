'''La siguiente fórmula permite convertir un valor de temperatura entre grados 
farenheit y grados celcius: 5 c (f 32) 9 = − 
Escriba un programa con un menú para realizar la conversión en ambos casos:
Solución
Variables
c: temperatura en °C
f: temperatura en °F
x: opción seleccionada'''
#conversion de Temperaturas
while True:
    print('1)Convertir F a C')
    print('2)Convertir C a F')
    print('3)Salir')
    x=input('Elija una opcion ')
    if x=='1':
        f=int(input('Ingrese grados F: '))
        c=5/9*(f*32)
        print(c)
    elif x=='2':
        c=int(input('Ingrese grados C: '))
        f=9/5*c+32
        print(f)
    elif x=='3:':
        print('Adios')
        break


