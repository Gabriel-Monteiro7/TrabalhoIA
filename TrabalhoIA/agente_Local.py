from copy import deepcopy
from No import No
from main_Rainha import Rainha
import time
# 1 == Largura #2 == Profundidade #3 == Custo Uniforme
# ultimo parametro é o tipo de busca se for por profundidade
# [] = se for lista de visitados
# int se for limitado
# Object se for interativa
# Problema(mapaRomenia.opcao(),origem,destino,2,[])

class AgenteLocal:
    def __init__(self,quant,tipoProblema,tipoBusca):
        self.tipoProblema = tipoProblema
        if(self.tipoProblema==1):
            Rainha(quant)
        self.quant = quant
        borda = []
        borda.append(No(gerarMatriz(quant), None))
        buscaLocal(self,borda,tipoBusca)
        
def gerarMatriz(quant):
    matriz = []
    for c in range(quant):
        linha = []
        for l in range(quant):
            linha.append("*")
        matriz.append(linha)
    return matriz

def expande(self,estadoAtual,linha):
    vetor = []
    for coluna in range(self.quant):
        isSalve = True
        if(estadoAtual.estado[coluna][linha] == "*"):
            if(self.tipoProblema==1):
                aux = Rainha.testeDeColisao(self,estadoAtual.estado, coluna, linha)
            for item in aux:
                if("G" in item):
                    isSalve = False
                    break
            if(isSalve):
                aux = deepcopy(estadoAtual.estado)
                aux[coluna][linha] = "G"
                vetor.append(No(aux, estadoAtual))
    return vetor


def sucessoraLargura(self,estadoAtual,linha,borda):
    aux = expande(self,estadoAtual, linha)
    for item in aux:
        borda.append(No(item.estado, estadoAtual))
    return borda


def sucessoraProfundidade(self,estadoAtual,linha,borda):
    aux = expande(self,estadoAtual, linha)
    for item in aux:
        borda.insert(0,No(item.estado, estadoAtual))
    return borda


def testeDeObjetividade(self,estadoAtual, combinacoes,borda,tipoBusca):
    if(estadoAtual.getProfundidade() == self.quant):
        combinacoes.append(estadoAtual)
        if(tipoBusca==1):
            for item in borda:
                combinacoes.append(item)
        return True
    else:
        return False
            
def mostraResultado(resultado,tempoTotal):
    print("Quantidade de resultados:",resultado.__len__())
    while(resultado[0]!=None):
        print("Profundida:",resultado[0].getProfundidade())
        for item in resultado[0].estado:
            print(item)
        print("")
        resultado[0] = resultado[0].pai
    print("Tempo total: %0.1f" % tempoTotal, "ms")

def buscaLocal(self,estadoInicial,tipoBusca):
    combinacoes = []
    borda = estadoInicial
    linha = 0
    inicio = time.time()
    while(linha <= self.quant):
        estadoAtual = borda[0]
        borda.pop(0)
        count = 0
        for item in estadoAtual.estado:
            if("G" in item):
                count += 1
        linha = count
        if(testeDeObjetividade(self,estadoAtual,combinacoes,borda,tipoBusca)):
            fim = time.time()
            mostraResultado(combinacoes,tempoTotal = (fim - inicio)*1000)
            break
        if(tipoBusca == 1):
            borda = sucessoraLargura(self,estadoAtual,linha,borda)
        else:
            borda = sucessoraProfundidade(self,estadoAtual, linha,borda)




