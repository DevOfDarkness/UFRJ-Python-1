#1
def qtd_palavras(frase):
    """Função que retorna a quantidade de palavras"""
    s = str.split(frase,' ')
    return len(s)

#2
def frase_posicoes(frase,palavra,p1,p2):
    """Função que retorna a frase excluindo-se
    as ocorrências desta palavra entre as posições p1 e p2"""
    s = str.strip(frase[p1:p2+1:])
    if s == palavra:
        return str.replace(frase,palavra,'')
    else:
        return frase

#3
def dada_frase(frase):
    """Função que dada uma frase substitui todos os seus caracteres
    em branco por #"""
    s1 = str.split(frase,' ')
    s = str.join("#",(s1))
    return s

#4
def trecho(palavra,caractere):
    """Função que retorna o trecho da string entre o caractere e o final"""
    indice = str.find(palavra,caractere)
    return palavra[indice+1:]


#5
def duas_tuplas(tupla,elem = 0):
    """Retorna duas tuplas
    A primeira apenas com strings e a segunda apenas os inteiros"""
    if type(tupla[0]) == str and (tupla[1] and tupla[2]) == int or float or complex:
        return tupla[0], (tupla[1],tupla[2])
    elif type(tupla[1])==str and (tupla[0] and tupla[2]) == int or float or complex :
        return tupla[1], (tupla[0],tupla[2])
    elif type(tupla[2])==str and (tupla[1] and tupla[0]) == int or float or complex:
        return tupla[2], (tupla[0],tupla[1])
    elif type(tupla[0]) and type(tupla[1]) == str:
        return (tupla[0],tupla[1]), tupla[2]
    elif type(tupla[0]) and type(tupla[2]) == str:
        return (tupla[0],tupla[2]), tupla[1]
    elif type(tupla[1]) and type(tupla[2]) == str:
        return (tupla[1],tupla[2]), tupla[0]
    elif type(tupla[0]) and type(tupla[1]) and type(tupla[2]) == str:
        return (tupla[0],tupla[1],tupla[2]), ()
    else:
        return tupla
        
    
#6
def listas(L1,L2):
    """Retorna duas listas intercaladas"""
    return L1[0],L2[0],L1[1],L2[1],L1[2],L2[2]
