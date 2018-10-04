# -*- coding: utf-8 -*-
from no import No

class ProblemaAspirador(object):

    def __init__(self, inicio):
        
        self.estadoInicial = inicio
     

    def acoes(self, estado):
        return ['Aspirar', 'Esquerda', 'Direita']
    
    def funcaoSucessora(self, estado, acao):
        
        lista = [['ELL','Aspirar','ELL'],
                 ['ELL','Esquerda','ELL'],
                 ['ELL','Direita','DLL'],

                 ['ELS','Aspirar','ELS'],
                 ['ELS','Esquerda','ELS'],
                 ['ELS','Direita','DLS'],
                 
                 ['ESL','Aspirar','ELL'],
                 ['ESL','Esquerda','ESL'],
                 ['ESL','Direita','DSL'],
                 
                 ['ESS','Aspirar','ELS'],
                 ['ESS','Esquerda','ESS'],
                 ['ESS','Direita','DSS'],
                 
                 ['DLL','Aspirar','DLL'],
                 ['DLL','Esquerda','ELL'],
                 ['DLL','Direita','DLL'],
                 
                 ['DLS','Aspirar','DLL'],
                 ['DLS','Esquerda','ELS'],
                 ['DLS','Direita','DLS'],
                 
                 ['DSL','Aspirar','DSL'],
                 ['DSL','Esquerda','ESL'],
                 ['DSL','Direita','DSL'],
                 
                 ['DSS','Aspirar','DSL'],
                 ['DSS','Esquerda','ESS'],
                 ['DSS','Direita','DSS']]
        
        for i in lista:
            if (estado == i[0] and acao == i[1]):
                return i[2]
        
        return ('Erro na função sucessora!')

    def testeDeObjetivo(self, estado):
        if(estado == 'ELL' or estado == 'DLL'):
            return True
        return False
    
    def custoDoPasso(self, pai, filho):
        return 1
