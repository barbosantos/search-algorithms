# -*- coding: utf-8 -*-

class No:
    def __init__(self, estado):
        self.estado = estado
        self.pai = None
        self.acao = None
        self.custo = 0    
    
    def setEstado(self, estado):
        self.estado = estado
    
    def getEstado(self):
        return self.estado
    
    def setPai(self, pai):
        self.pai = pai
        
    def getPai(self):
        return self.pai
    
    def setCusto(self, custo):
        self.custo = custo

    def getCusto(self):
        return self.custo
    
    def setAcao(self, acao):
        self.acao = acao

    def getAcao(self):
        return self.acao
    
    def __repr__(self):
        return "Estado: {}\nPai: {}\nCusto: {}\nAção: {}".format(self.estado,self.pai.estado,self.custo,self.acao)   
    
    def printar(self):
        print('Estado: ', self.estado, '\nPai:', self.pai, '\nCusto:', self.custo, '\nAção:', self.acao)
    
    def printarEstado(self):
        print('Estado: ', self.estado)
       