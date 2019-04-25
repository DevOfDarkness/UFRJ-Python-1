#1
def f_inversa(frase):
    """Função que retorna uma frase invertida"""
    f = str.split(frase,' ')
    reverte = list.reverse(f)
    return str.join(' ',f)

#2
def alfabetica(frase):
    """Função que ordena em ordem alfabética"""
    f = str.split(frase,' ')
    ordena = list.sort(f)
    return str.join(' ',f)

#3
def troca_vogais(frase):
    """Função que troca as vogais por i"""
    s =  str.replace(frase,'a','i').replace('e','i').replace('o','i').replace('u','i')
    return s

#4
def frase(frase,palavra,posicao):
    """Função que faz alguma coisa com uma frase e uma palavra"""
    if palavra in frase:
        m = str.upper(palavra)
        return str.replace(frase,palavra,m)
    else:
        f = str.split(frase,' ')
        list.insert(f,posicao,palavra)
        return str.join(' ',f)

#5
def faltas(lista):
    """Função que retorna um número de faltas"""
    faltas = lista[0][2][1]+lista[1][2][1]+lista[2][2][1]
    return "Total de "+str(faltas)+" faltas"

#6
def inclui_n(lista,n):
    """Função que insere um n numa lista"""
    lista.append(n)
    lista.sort()
    return lista

#7
def sub_lista(lista,n):
    """Função que faz mais coisas com listas"""
    lista.sort()
    indice = lista.index(n)
    return lista[indice+1:]

#8
def maior_elemento(lista):
    """Função que retorna o maior número da lista"""
    lista.sort()
    return lista[-1]

#9
def media(lista):
    """Função que retorna a média das notas, e quais ficaram acima da média"""
    media = sum(lista)//len(lista)
    lista.sort()
    return list((sum(lista)/len(lista),sub_lista(lista,media)))

#10
def colchao(colchao,h,l):
    """Função que compara o colchão com a porta"""
    if colchao[1] <= h:
        return True
    else:
        return False
