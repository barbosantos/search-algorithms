# -*- coding: utf-8 -*-
from problemaMapa import *
from problemaAspirador import *
from estruturaDeDados import *
from no import *

#Início da função
def BFS(problema):
    
    no = No(problema.estadoInicial)
    
    if(problema.testeDeObjetivo(no.estado)):
        print('*** Solução Trivial! ***')
        return solucao(no,[])
        
    borda = Fila()
    borda.adicionar(no)
    explorado = []

    while(not borda.vazia()):
        
        print('*** BORDA ***')
        borda.printar()        
        
        no = borda.remove()
        
        explorado.append(no.estado)
        
        for acao in problema.acoes(no.estado):
            
            filho = noFilho(problema, no, acao)

            if(filho.estado not in explorado and filho not in borda):
                if(problema.testeDeObjetivo(filho.estado)):
                    print('*** Solução Encontrada! ***')
                    return solucao(filho, [])
                borda.adicionar(filho)
#Término da função             


#Início da função
def DFS(problema):
    
    no = No(problema.estadoInicial)
    
    if(problema.testeDeObjetivo(no.estado)):
        print('*** Solução Trivial! ***')
        return no
        #return solucao(no) #Implementar
        
    borda = Pilha()
    borda.adicionar(no)
    explorado = []

    while(not borda.vazia()):
        
        print('*** BORDA ***')
        borda.printar()          
        
        no = borda.remove()
        
        explorado.append(no.estado)
        
        for acao in problema.acoes(no.estado):
            
            filho = noFilho(problema, no, acao)

            if(filho.estado not in explorado and filho not in borda):
                if(problema.testeDeObjetivo(filho.estado)):
                    print('*** Solução Encontrada! ***')
                    return solucao(filho, [])
                borda.adicionar(filho)
#Término da função 

#Início da função
def noFilho(problema, pai, acao):
    no = No(problema.funcaoSucessora(pai.estado,acao))
    no.setPai(pai)
    no.setAcao(acao)
    no.setCusto(problema.custoDoPasso(pai.estado,no.estado) + pai.custo)
    
    return no
#Término da função  

#Função para retornar a lista da solução
def solucao(no, move):
    move.append(no.estado + ' --> ')
    if(no.pai == None):
        return move
    #move.append(no.estado)
    print('---------------------')
    print('Estado do nó: ',no.getEstado())
    #print('Custo do nó: ',no.getCusto())
    print('Ação do nó: ',no.getAcao())
    aux = solucao(no.pai, move)
    return aux[::-1]
#Fim da função


#Início da função
def CustoUniforme(problema):
    
    no = No(problema.estadoInicial)
        
    borda = FilaDePrioridade()
    borda.adicionar(no)
    
    explorado = []

    while(not borda.vazia()):
        
        #print('*** BORDA ***')
        #borda.printar()        
        
        no = borda.remove()
        
        if(problema.testeDeObjetivo(no.estado)):
            print('*** Solução Encontrada! ***')
            return solucao(no,[])
        
        explorado.append(no.estado)
        
        for acao in problema.acoes(no.estado):
            
            filho = noFilho(problema, no, acao)

            if(filho.estado not in explorado and filho not in borda):
                borda.adicionar(filho)
            
            condicao,indice = inBorda(filho, borda)    
            if(condicao):
                borda.retira(indice)
                borda.adicionar(filho)
#Término da função

#Início da função
def inBorda(noFilho, borda):
    for indice,no in enumerate(borda):
        if(noFilho.estado == no.estado and noFilho.custo < no.custo):
            return True, indice
    return False, 0
#Término da função

#Início da função
def aEstrela(problema):
    
    no = No(problema.estadoInicial)
        
    borda = FilaDePrioridade()
    borda.adicionar(no)
    
    explorado = []

    while(not borda.vazia()):
        
        #print('*** BORDA ***')
        #borda.printar()        
        
        no = borda.remove()
        
        if(problema.testeDeObjetivo(no.estado)):
            print('*** Solução Encontrada! ***')
            return solucao(no,[])
        
        explorado.append(no.estado)
        
        for acao in problema.acoes(no.estado):
            
            filho = noFilhoEstrela(problema, no, acao)

            if(filho.estado not in explorado and filho not in borda):
                borda.adicionar(filho)
            
            condicao,indice = inBorda(filho, borda)    
            if(condicao):
                borda.retira(indice)
                borda.adicionar(filho)
#Término da função

#Início da função
def noFilhoEstrela(problema, pai, acao):
    no = No(problema.funcaoSucessora(pai.estado,acao))
    no.setPai(pai)
    no.setAcao(acao)
    no.setCusto(problema.custoDoPasso(pai.estado,no.estado) + pai.custo + problema.heuristica(no.estado))
    
    return no
#Término da função

#Início da função
def guloso(problema):
    
    no = No(problema.estadoInicial)
        
    borda = FilaDePrioridade()
    borda.adicionar(no)
    
    explorado = []

    while(not borda.vazia()):
        
        #print('*** BORDA ***')
        #borda.printar()        
        
        no = borda.remove()
        
        if(problema.testeDeObjetivo(no.estado)):
            print('*** Solução Encontrada! ***')
            return solucao(no,[])
        
        explorado.append(no.estado)
        
        for acao in problema.acoes(no.estado):
            
            filho = noFilhoGuloso(problema, no, acao)

            if(filho.estado not in explorado and filho not in borda):
                borda.adicionar(filho)
            
            condicao,indice = inBorda(filho, borda)    
            if(condicao):
                borda.retira(indice)
                borda.adicionar(filho)
#Término da função

#Início da função
def noFilhoGuloso(problema, pai, acao):
    no = No(problema.funcaoSucessora(pai.estado,acao))
    no.setPai(pai)
    no.setAcao(acao)
    no.setCusto(problema.heuristica(no.estado))
    
    return no
#Término da função 