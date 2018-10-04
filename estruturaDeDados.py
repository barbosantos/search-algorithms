# -*- coding: utf-8 -*-
from no import *

#Inicio da classe
class Fila:
    def __init__(self):
        self.list = []
        
    #Insere no final
    def adicionar(self,item):
        self.list.append(item)
    
    #Remove no começo
    def remove(self):
        return self.list.pop(0)

    def vazia(self):
        return len(self.list) == 0

    def __contains__(self, item):
        return item in self.list
    
    def printar(self):
        for i in self.list:
            i.printarEstado()
#Fim da classe

#Inicio da classe
class Pilha:
    def __init__(self):
        self.list = []
    
    #Insere no final
    def adicionar(self,item):
        self.list.append(item)
    
    #Remove no final
    def remove(self):
        return self.list.pop()

    def vazia(self):
        return len(self.list) == 0

    def __contains__(self, item):
        return item in self.list
    
    def printar(self):
        for i in self.list:
            i.printarEstado()
#Fim da classe

#Inicio da classe
class FilaDePrioridade:
    
    def __init__(self):
        self.list = []

    def adicionar(self,item):
        self.list.append(item)

    def vazia(self):
        return (len(self.list) == 0)

    def __contains__(self, item):
        return (item in self.list)
    
    #Remove sempre o nó de menor custo
    def remove(self):
        menori = 0
        for i in range(1,len(self.list)):
            if (self.list[i].custo < self.list[menori].custo):
                menori = i
        item = self.list[menori]
        self.list[menori:menori+1] = []
        return item
    
    def printar(self):
        for i in self.list:
            i.printarEstado()
    
    def tamanho(self):
        return len(self.list)
    
    def retira(self, indice):
        return self.list.pop(indice)
    
    def __iter__(self):
        for x in self.list:
            yield x    
#Fim da classe

#Teste
'''
borda = Pilha()
borda.adicionar(2)
borda.adicionar(4)
borda.adicionar(7)
borda.adicionar(1)
print('------------')
borda.printar()
borda.remove()
print('------------')
borda.printar()
'''

