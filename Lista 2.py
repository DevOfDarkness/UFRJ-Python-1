from math import *

#1
#a
def media_2numeros (a,b):
    """Função que calcula a média de dois números"""
    return (a+b)/2

def media_4numeros(a,b,c,d):
    """Função que calcula a média de 4 números"""
    return (media_2numeros(a,b)+media_2numeros(c,d))//2

#b
def joaozinho (d,p):
    """Função que retorna bombons e o troco"""
    #d = dinheiro
    #p = preço
    bombons = d//p
    troco = d-p*bombons
    return bombons,troco

#2
#a
def hipotenusa(b,c):
    """Função que calcula a hipotenusa
    dados os catetos b e c"""
    hipotenusa = sqrt(b**2+c**2)
    return hipotenusa

#b
def distancia(xb,xa,yb,ya):
    """Função que calcula a distancia
    de dois pontos num plano dadas suas coordenadas"""
    distancia = sqrt((xb-xa)**2+(yb-ya)**2)
    return distancia

#c
def perimetro_triangulo(a,b):
    """Função que calcula o perímetro
    do triângulo retângulo dados os catetos a e b"""
    return hipotenusa(a,b)+a+b

#d
def soma_sen_cos(a):
    """Função que soma o quadrado do seno e cosseno
    dado o ângulo a"""
    #para a = 360 o retorno é igual a 1
    soma = (sin(a))**2+(cos(a))**2
    return soma

#3
def circulo_perimetro(r):
    """Função que calcula o perímetro do círculo
    dado seu raio"""
    #r = raio
    return 2*pi*r

#4
def voltas(r,d):
    """Função que calcula quantas voltas um atleta
    deu em uma pista circular"""
    #r = raio
    #d = distancia

    #r = 100
    #d = 600000
    #return = 955 voltas
    return d/circulo_perimetro(r)

#5
def delta_raiz(a,b,c):
    """Função que calcula o delta
    e retorn as raizes reais de uma equação do 2º grau"""
    delta = b**2-4*a*c
    x1 = (-b+sqrt(delta))//(2*a)
    x2 = (-b-sqrt(delta))//(2*a)
    return delta, x1, x2

#6
def setor_circular(r,a=360):
    """Função que calcula a área do setor circular
    caso informado o angulo"""
    #r = raio
    #a = angulo a ser informado  
    area_setor = (a*3.14*r**2)/360
    return area_setor

#7
def soma_final(an,a1,r):
    """Função que calcula a soma final de uma PA"""
    s = soma((a1+an)*termos(an,a1))/2
    return s
#a
def termos(an,a1):
    """Função que calcula os n termos de uma PA"""
    n = ((an-a1)/r)+1
    return n

#b
def soma(an,a1,n):
    """Função que soma uma PA"""
    Sn = ((a1+an)*n)/2
    return Sn

#8
def bolos(a,b,c):
    """Função que calcula quantos bolos joão pode fazer"""
    #a = xícaras
    #b = ovos
    #c = leite
    bolo = ((a//2)+(b//3)+(c//5))//3
    return bolo


