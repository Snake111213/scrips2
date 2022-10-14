'''Ejemplo. Defina un módulo (librería) con el nombre geometría que contenga funciones 
con algunas fórmulas de la geometría básica para calcular área y volumen. Incluya
fórmulas para el círculo, sector de círculo, segmento de círculo, esfera, cilindro y cono'''

from math import*
from re import S
def circulo(r):
    s=pi*r**2
    return S

def sector(r,a):
    s=pi*r**2*a
    return S

def segmento(r,a):
    s=r**2*(pi*a-0.5*sin(a))
    return

def cilindro(r,h):
    s=2*pi*r*(r+h)
    v=pi*r**2*h
    return [s,v]

def cono(r,h):
    g=sqrt(h**2+r**2)
    s=pi*r*g*+pi*r**2
    v=pi*r**2*h/3
    return [s,v]

print(cilindro==9)