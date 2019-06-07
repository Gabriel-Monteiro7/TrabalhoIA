from no import No
from rainhas import Rainha

import time
# 1 == Largura #2 == Profundidade #3 == Custo Uniforme
# ultimo parametro é o tipo de busca se for por profundidade
# [] = se for lista de visitados
# int se for limitado
# Object se for interativa
# Problema(mapaRomenia.opcao(),origem,destino,2,[])

class AgenteLocal():
    def __init__(self,quantidade,tipoBusca,tipoProfundidade=None,estadoInicial=None,estadoFinal=None,tipoProblema=None):
        self.tipoProblema = tipoProblema
        self.tipoBusca = tipoBusca
        self.estadoInicial = estadoInicial
        self.estadoFinal  = estadoFinal
        self.quantidade = quantidade
        self.tipoProfundidade = tipoProfundidade
        borda = []
        borda.append(estadoInicial)
        buscaLocal(self,borda)

def buscaLocal(self,estadoInicial):
    combinacoes = []
    borda = estadoInicial
    linha = 0
    inicio = time.time()
    passos = 0
    while(True):
        passos+=1
        print("Quantidade de passos:",passos)
        if(borda==[]):
            break
        else:
            estadoAtual = borda[0]
            self.tipoProfundidade.append(estadoAtual.estado)
            borda.pop(0)
        if(estadoAtual.testeDeObjetividade(estadoAtual,self.estadoFinal,combinacoes,borda)):
            fim = time.time()
            tempoTotal = (fim - inicio)*1000
            estadoAtual.mostraResultado(combinacoes,tempoTotal,self.estadoInicial)
            break
        borda = estadoAtual.sucessora(estadoAtual,borda,self.tipoBusca,self.tipoProblema,self.tipoProfundidade)
        




