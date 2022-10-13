#Compra de llantas con descuento
n=int(input('Cantidad de llantas: '))
p=float(input('Precio unitario: '))
if n>4:
    p=0.9*p
    t=n*p
    print('Valor a pagar: ',t)