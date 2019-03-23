#1
def areaRetangulo(b,h):
    #Função que retorna a área de um retângulo
    return b*h

#2
def areaCirculo(r):
    #Função que calcula a área de um círculo
    pi = 3.1415
    return pi*r**2

def areaCoroa(r1,r2):
    #Função que calcula a area da coroa
    return areaCirculo(r1) - areaCirculo(r2)

#3
def div_Resto(n,d):
    #Função que retorna divisão e resto
    return n//d,n%d

#4
def ordenada_2grau(a,b,x,c):
    #Função que retorna a ordenada e as abscissas
    delta = b**2-4*a*c
    x1 = (-b + delta**1/2)/(2*a)
    x2 = (-b - delta**1/2)/(2*a)
    return a*x**2+b*x+c, x1, x2
    
#5
def gorjeta(g):
    #Função que calcula a gorjeta do garçom
    return (g*10)/100

#6
def media(a,b):
    #Função que calcula a média de dois números
    return (a+b)/2

#7
def media_Ponderada(n1,p1,n2,p2):
    #Função que calcula a média ponderada de dois números
    return (n1*p1+n2*p2)/(p1+p2)

#8
def distancia(vc,lr,vb):
    #Função que calcula a distância que a correnteza arrasta um barco
    velocidade_travessia = vb-vc
    tempo_travessia = lr/velocidade_travessia
    return tempo_travessia*vc

#9
def saldo(si,meses,juros):
    #Função que calcula o saldo final
    taxa = juros/100
    saldo_Final = si*(1+taxa*meses)
    return saldo_Final

#10
def erro_pg(q,n):
    #Função que calcula o erro da PG
    pg = 1/(1-q)
    sn = 1*(q**n-1)/(q-1)
    return pg - sn

#11
def tempo_total(hh,mm,ss,h,m,s):
    #Função que calcula o tempo de prova em minutos
    tempo_total = (h*60+mm+s//60)-(hh*60+mm+ss//60)
    return print("O tempo total de prova foi de",tempo_total,"minutos")

#12
def valor_gorjeta(conta,pessoas):
    #Função que calcula quanto cada pessoa vai pagar na gorjeta
    gorjeta = conta*0.1
    return gorjeta/pessoas

#13
def area_cubo(c):
    #Função que cálcula a área do cubo
    area_Total = 6*c**2
    return area_Total
