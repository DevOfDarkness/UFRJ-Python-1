#1
from math import *

def absoluto(x):
    """Função que retorna o valor absoluto de um número"""
    if x < 0:
        return x*-1
    else:
        return x

#2
def raizes(a,b,c):
    """Função que retorna as raízes do 2º grau"""
    delta = b**2-4*a*c
    #1º caso entrada a = 1 b = -3 e c = -10 retorno x1 = -2 e x2 = 5
    #2º caso entrada a = 5 b = 3 e c = 4 retorno, sem raízes reais
    #3º caso entrada a = 9 b = -2 e c =  4 retorno x = 2/3 ou x = 0,66666...
    

    if delta > 0:
        return "A equação possui as raizes x1 = "+str((-b-sqrt(delta))//(2*a))+ " e x2 = "+str((-b+sqrt(delta))//(2*a))
    elif delta == 0:
        return "A equação possui somente a raiz x = "+str((-b-sqrt(delta))/(2*a))
    else:
        return "A equação não possui raízes reais"

#3
def palavra(p):
    """Função que retorna a palavra repetiva 3 vezes"""
    return p*3

#4
def funcao(x):
    """Função matemática"""
    #Foram necessários 8 casos de teste com cada ponto de x no gráfico e para valores que x não está definido
    #Para 0 <= x <= 2, o retorno é uma reta do tipo y = x
    #x = 0 -> y = 0, x = 1 -> y = 1, x = 2 -> y = 2

    #Para 2 < x <= 3.5, o retorno é a constante y = 2
    #x = 3 -> y = 2, x = 3.1 -> y = 2, x = 3.5 -> y = 2

    #Para 3.5 < x <= 5, o retorno é a constante y = 3
    #x = 4 -> y = 3, x = 5 -> y = 3

    #Para 5 < x <= 6, o retorno é o cálculo efetuado pela função x²-10x+28

    #Para x > 6 a função retorna um aviso dizendo que está fora do domínio
    
    if x >= 0 and x <= 2:
        return "y = "+str(x)
    elif x > 2 and x <= 3.5:
        return "y = "+str(2)
    elif x > 3.5 and x <=5:
        return "y = "+str(3)
    elif x > 5 and x <=6:
        return "y = "+str(x**2-10*x+28)
    elif x > 6:
        return "A função só está definida para x entre 0 e 6"
    
#5
def mdc(a,b):
    """Função que calcula o mdc entre dois números"""
    if (b == 0):
      return a
    else:
      return mdc(b, a % b)

def mmc(a,b):
    """Função que cálcula o mmc entre dois números"""
    if mdc(a,b) != 0:
        return (a*b)//(mdc(a,b))
    else:
        return "O mdc deve ser diferente de zero"

def mmc_e_mdc(a,b):
    """Função que chama mmc e mdc"""
    return "Máximo = "+str(mmc(a,b)), "Mínimo = "+str(mdc(a,b))

#6
def meia_entrada(idade,carteira):
    """Função que retorna o direito a meia entrada"""
    #carteira tem que ser um valor booleano, True para sim e False para não

    if idade >= 65 or idade < 21:
        return "Direito a meia entrada"
    elif idade >= 21 and carteira == True:
        return "Direito a meia entrada"
    elif idade >=65 or carteira == True:
        return "Direito a meia entrada"
    elif idade >= 21 and carteira == False:
        return "Sem direito a meia entrada"

#7
def campeonato(C,Ce,Cs,Fv,Fe,Fs):
    """Função que retorna o resultado do campeonato entre Cormengo e Flaminthias"""

    """Entrada: C -> Número de vitórias do Cormengo, Ce -> Número de empates do Cormengo, -> Cs -> Saldo de gold do Cormengo
    Fv -> Número de vitórias do Flaminthias, Fs -> Número de empates do Flaminthias, Fs -> Salod de golds do Flaminthias"""

    """Saída: A função retorna |Cormengo| se este estiver melhor classificado que o Flaminthias
    |Flaminthias| se este estiver melhor classificado que o Cormengo
    |Empate| caso ambos estejam empatados na tabela"""
    
    #Entrada: 10,5,18,11,2,18 -> Saída: ’Empate’
    #Entrada: 10,5,18,11,1,18 -> Saída: ’Cormengo’
    #Entrada: 9,5,-1,10,2,10 -> Saída: ’Flaminthias’

    pts_c = C*3+Ce
    pts_f = Fv*3+Fe

    if pts_f > pts_c:
        return "Flaminthias"
    elif pts_f == pts_c and Cs == Fs:
        return "Empate"
    elif pts_f == pts_c and Fs > Cs:
        return "Flaminthias"
    else:
        return "Cormengo"

#8
def aviao_de_papel(C,Qp,Qf):
    """Função que retorna se dá pra fazer um avião de papel dados os parâmetros
    C = Competidores, Qp = Quantidade de Papel e Qf = Quantidade de folhas"""
    #Entrada 10,100,10 -> Saída: "Suficiente"
    #Entrada: 10,90,10 -> Saída: "Insuficiente"
    #Entrada: 5,10,2 -> Saída: "Suficiente"

    if Qf*C > Qp:
        return "Insuficiente"
    else:
        return "Suficiente"
    
    
