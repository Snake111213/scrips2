
'''Escriba una función recursiva para contar en cuantos intentos se puede 
adivinar el número de un dado.'''
from random import*
def adivina(intento):
    n=randint(1,6)
    x=int(input('Adivina el numero: '))
    if x!=n:
        print('Fallaste: intenta otra vez')
        intento=intento+1
        adivina(intento)
    else:
        print('Acertaste en ', intento)