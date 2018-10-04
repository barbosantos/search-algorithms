# -*- coding: utf-8 -*-
from no import No

class ProblemaMapa(object):

    def __init__(self, inicio, objetivo):
        
        self.estadoInicial = inicio
        self.estadoObjetivo = objetivo
        
        self.ARAD = No('Arad')
        self.BUCHAREST = No('Bucharest')
        self.CRAIOVA = No('Craiova')
        self.GIURGIU = No('Giurgiu')
        self.HIRSOVA = No('Hirsova')
        self.IASI = No('Iasi')
        self.LUGOJ = No('Lugoj')
        self.MEHADIA = No('Mehadia')
        self.NEAMT = No('Neamt')
        self.ORADEA = No('Oradea')
        self.PITESTI = No('Pitesti')
        self.RIMNICU_VILCEA = No('Rimnicu_Vilcea')
        self.SIBIU = No('Sibiu')
        self.TIMISOARA = No('Timisoara')
        self.URZICENI = No('Urziceni')
        self.VASLUI = No('Vaslui')
        self.ZERIND = No('Zerind')
        self.FAGARAS = No('Fagaras')
        self.DOBRETA = No('Dobreta')
        self.EFORIE = No('Eforie')        

    def acoes(self, estado):
        acoes = {'Arad':['IrTimisoara','IrZerind','IrSibiu'],
                 'Bucharest':['IrFagaras','IrPitesti','IrGiurgiu','IrUrziceni'],
                 'Craiova':['IrDobreta','IrRimnicu_Vilcea','IrPitesti'],
                 'Giurgiu':['IrBucharest'],
                 'Hirsova':['IrUrziceni','IrEforie'],
                 'Iasi':['IrNeamt','IrVaslui'],
                 'Lugoj':['IrMehadia','IrTimisoara'],
                 'Mehadia':['IrLugoj','IrDobreta'],
                 'Neamt':['IrIasi'],
                 'Oradea':['IrZerind','IrSibiu'],
                 'Pitesti':['IrRimnicu_Vilcea','IrBucharest','IrCraiova'],
                 'Rimnicu_Vilcea':['IrSibiu','IrPitesti','IrCraiova'],
                 'Sibiu':['IrArad','IrRimnicu_Vilcea','IrOradea','IrFagaras'],
                 'Timisoara':['IrArad','IrLugoj'],
                 'Urziceni':['IrBucharest','IrVaslui','IrHirsova'],
                 'Vaslui':['IrIasi','IrUrziceni'],
                 'Zerind':['IrOradea','IrArad'],
                 'Fagaras':['IrSibiu','IrBucharest'],
                 'Dobreta':['IrMehadia','IrCraiova'],
                 'Eforie':['IrHirsova']}
        return acoes[estado]
    
    def funcaoSucessora(self, estado, acao):
        return acao[2:]
        

    def testeDeObjetivo(self, estado):
        if(self.estadoObjetivo == estado):
            return True
        return False
    
    def custoDoPasso(self, pai, filho):
        lista = [['Arad','Timisoara',118],
                 ['Arad','Zerind',75],
                 ['Arad','Sibiu',140],
                 ['Bucharest','Fagaras', 211],
                 ['Bucharest', 'Pitesti', 101],
                 ['Bucharest', 'Giurgiu', 90],
                 ['Bucharest', 'Urziceni', 85],
                 ['Craiova','Dobreta', 120],
                 ['Craiova', 'Rimnicu_Vilcea', 146],
                 ['Craiova', 'Pitesti', 138],
                 ['Giurgiu', 'Bucharest', 90],
                 ['Hirsova', 'Urziceni', 98],
                 ['Hirsova', 'Eforie', 86],
                 ['Iasi', 'Neamt', 87],
                 ['Iasi', 'Vaslui', 92],
                 ['Lugoj', 'Mehadia', 70],
                 ['Lugoj', 'Timisoara', 111],
                 ['Mehadia', 'Lugoj', 70],
                 ['Mehadia', 'Dobreta', 75],
                 ['Neamt', 'Iasi', 87],
                 ['Oradea', 'Zerind', 71],
                 ['Oradea', 'Sibiu', 151],
                 ['Pitesti', 'Rimnicu_Vilcea', 97],
                 ['Pitesti', 'Bucharest', 101],
                 ['Pitesti', 'Craiova', 138],
                 ['Rimnicu_Vilcea', 'Sibiu', 80],
                 ['Rimnicu_Vilcea', 'Pitesti', 97],
                 ['Rimnicu_Vilcea', 'Craiova', 146],
                 ['Sibiu', 'Arad', 140],
                 ['Sibiu', 'Rimnicu_Vilcea', 80],
                 ['Sibiu', 'Oradea', 151],
                 ['Sibiu', 'Fagaras', 99],
                 ['Timisoara', 'Arad', 118],
                 ['Timisoara', 'Lugoj', 111],
                 ['Urziceni', 'Bucharest', 85],
                 ['Urziceni', 'Vaslui', 142],
                 ['Urziceni', 'Hirsova', 98],
                 ['Vaslui', 'Iasi', 92],
                 ['Vaslui', 'Urziceni', 142],
                 ['Zerind', 'Oradea', 71],
                 ['Zerind', 'Arad', 75],
                 ['Fagaras', 'Sibiu', 99],
                 ['Fagaras', 'Bucharest', 211],
                 ['Dobreta', 'Mehadia', 75],
                 ['Dobreta', 'Craiova', 120],
                 ['Eforie','Hirsova', 86]]
 
        for i in lista:
            if (pai == i[0] and filho == i[1]):
                return i[2]
            
        return ('Erro na função de custo!')
    
    def heuristica(self, estado):
        
        lista = [['Arad',366],
                 ['Bucharest', 0],
                 ['Craiova', 160],
                 ['Giurgiu', 77],
                 ['Hirsova', 151],
                 ['Iasi',  226],
                 ['Lugoj', 244],
                 ['Mehadia', 241],
                 ['Neamt', 234],
                 ['Oradea', 380],
                 ['Pitesti', 100],
                 ['Rimnicu_Vilcea', 193],
                 ['Sibiu', 253],
                 ['Timisoara', 329],
                 ['Urziceni', 80],
                 ['Vaslui', 199],
                 ['Zerind', 374],
                 ['Fagaras', 176],
                 ['Dobreta', 242],
                 ['Eforie', 161]]
        
        for i in lista:
            if (estado == i[0]):
                return i[1]
            
        return ('Erro na função de custo!')