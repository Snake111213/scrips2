ns = int(input('Cuantas semanas: '))
nv = int(input('Cuantos vendedores: '))
na = int(input('Cuantos articulos: '))
c = []
for i in range(ns):
    s = []
    for j in range(nv):
        f = []
        for k in range(na):
            print('semana: ', i+1, 'Vendedor: ', j+1,' Articulo: ',k+1)
            x = int(input('Ingrese la cantidad vendida: '))
            f = f + [x]
        s = s + [f]
    c = c + [s]

for i in range(ns):
    print('Semana: ',i + 1)
    for j in range(nv):
        t = t + c [i][j][k]
    print('Vendedor: ', j + 1, ' Total: ',t)