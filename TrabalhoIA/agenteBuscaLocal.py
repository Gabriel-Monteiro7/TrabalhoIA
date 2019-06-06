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
    def __init__(self,quantidade,tipoBusca,estadoInicial,estadoFinal=None,tipoProblema=None):
        self.tipoProblema = tipoProblema
        self.tipoBusca = tipoBusca
        self.estaInicial = estadoInicial
        self.estadoFinal  = estadoFinal
        self.quantidade = quantidade
        borda = []
        borda.append(estadoInicial)
        buscaLocal(self,borda)

def buscaLocal(self,estadoInicial):
    combinacoes = []
    borda = estadoInicial
    linha = 0
    inicio = time.time()

    while(True):
        
        if(borda==[]):
            break
        else:
            estadoAtual = borda[0]
            borda.pop(0)
        if(estadoAtual.testeDeObjetividade(estadoAtual,self.estadoFinal,combinacoes,borda)):
            fim = time.time()
            estadoAtual.mostraResultado(combinacoes,tempoTotal = (fim - inicio)*1000)
            break
        borda = estadoAtual.sucessora(estadoAtual,borda,self.tipoBusca,self.tipoProblema)
        




