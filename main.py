# -*- coding: utf-8 -*-
from algoritmosDeBusca import *

'''
#problema = ProblemaMapa('Sibiu','Bucharest')
#problema = ProblemaMapa('Arad','Neamt')
problema = ProblemaMapa('Arad','Bucharest')

resposta = BFS(problema)
#resposta = DFS(problema)
#resposta = CustoUniforme(problema)
#resposta = aEstrela(problema)
#resposta = guloso(problema)
print(resposta)
'''

problema = ProblemaAspirador('ESS')

resposta = BFS(problema)
#resposta = DFS(problema)
print(resposta)

