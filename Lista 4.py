#1
def conc_string(a,b):
    """Função que concatena duas strings a e b"""
    #entrada ab
    #retorno abba
    y = a+b
    return y+y[::-1]

#2
def num_sorte(nome,idade):
    """Função que retorna o número da sorte"""
    return "Parabéns "+nome+" seu número da sorte é "+str((((idade*4+8)*60)//240)+22-idade)

#3
def strings(s1,s2):
    """Função que concatena strings de até 15 caracteres"""
    if len(s1) and len(s2) <= 15:
        return s1[5:]+s2[0:5]
    else:
        return "As duas strings devem conter no mínimo 15 caracteres cada"

#4
def mais_strings(s,x,i):
    """Função que faz insere x numa posição da string"""
    #s = string | x = caractere qualquer | i = um inteiro entre 0 e o comprimento da string
    i = len(s)-1
    if i > 0:
        return s[:i]+x+s[i+1:]
    else:
        return "Insira um inteiro válido"

#5
def quanta_string(s):
    """Função que insere uma string no meio dela mesma"""
    metade = len(s)//2
    return s[:metade]+s+s[metade:]

#6
def func_string(s):
    """Função que insere # no ínicio, no meio e no final da string"""
    metade = len(s)//2
    return '#'+s[:metade]+'#'+s[metade:]+'#'

#7
def rotaciona_string(s):
    """Função que rotaciona uma string 3 posições para a esquerda"""
    return s[-3:]+s[:-3]

#8
def rotaciona_x(s,x):
    """Função que rotaciona a string x posições"""
    #s = string | x = um inteiro
    #saida string
    if x >= len(s):
        x = x-1
        return s[-x:]+s[:-x]
    else:
        return "A string deve ter pelo menos x caracteres"

#9
def rotaciona_x_2(s,x):
    """Outra função que faz a mesma coisa com strings mas x pode ser qualquer valor"""
    #s = string | x = um inteiro
    if x >= len(s):
        x = x-len(s)
        return s[-x:]+s[:-x]
    else:
        return s[-x:]+s[:-x]

#10
def duas_datas(data1,data2):
    """Função que calcula os dias, dadas as datas em strings"""
    dia1 = int(data1[0:2])
    mes1 = int(data1[3:5])*30
    ano1 = 366-(dia1+mes1)

    dia2 = int(data2[0:2])
    mes2 = int(data2[3:5])*30
    ano2 = 366-(dia2+mes2)
    return "O total de dias é: "+str(365-ano2 + ano1)

#11
def colisoes(R1x,R2y,R3x,R4y,R5x,R6y,R7x,R8y):
    """Função que retorna uma um valor booleano para caso haja colisão"""
    if R5x <= R3x:
        return True
    else:
        return False
        
