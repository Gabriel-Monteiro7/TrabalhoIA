from MapaDaRomenia import MapaDaRomenia
from Agente import Agente
from OitoPeca import OitoPeca
import random
from copy import deepcopy
from No import No
mapaRomenia = MapaDaRomenia()
origem = mapaRomenia.Oradea.estado
destino = mapaRomenia.Giurgiu.estado
listaVisitados = []
# 1 == Largura #2 == Profundidade #3 == Custo Uniforme
# ultimo parametro é o tipo de busca se for por profundidade
# [] = se for lista de visitados
# int se for limitado
# Object se for interativa
# Problema(mapaRomenia.opcao(),origem,destino,2,[])


def gerarMatriz(quant):
    matriz = []
    for c in range(quant):
        linha = []
        for l in range(quant):
            linha.append("*")
        matriz.append(linha)

    return matriz


def testeDeColisao(matriz, linha, coluna):
    col = []
    lin = []
    principal = []
    secundaria = []
    linhas = linha
    colunas = coluna
    count = 0
    for item in matriz:
        if(linha > coluna):
            if((linha-coluna)+count+1 <= quant):
                # achar a principal quando a linha>coluna
                principal.append(matriz[count+(linha-coluna)][count])
        else:
            if(coluna-linha+count+1 <= quant):
                # achar a principal quando a coluna>linha
                principal.append(matriz[count][count+(coluna-linha)])

        if(coluna+linha < quant):
            if(count <= coluna+linha):
                colunaAux = coluna+linha-count
                linhaAux = count
                # achar a secundaria quando a soma da linha e coluna for menor que o grau da matriz
                secundaria.append(matriz[linhaAux][colunaAux])
        elif(coluna+linha >= quant):
            if(count < (2*quant-linha-coluna-1)):
                colunaAux = linha+coluna-quant+count+1
                linhaAux = quant-1-count
                # achar a secundaria quando a soma da linha e coluna for maior que o grau da matriz
                secundaria.append(matriz[linhaAux][colunaAux])
        if(count == linhas):
            lin = item  # achar a linha da posicao
        count += 1
        col.append(item[colunas])  # achar a coluna da posicao
    vetor = [lin, col, principal, secundaria]
    return vetor


def expande(estadoAtual,linha):
    vetor = []
    for coluna in range(quant):
        isSalve = True
        if(estadoAtual.estado[coluna][linha] == "*"):
            aux = testeDeColisao(estadoAtual.estado, coluna, linha)
            for item in aux:
                if("G" in item):
                    isSalve = False
                    break
            if(isSalve):
                aux = deepcopy(estadoAtual.estado)
                aux[coluna][linha] = "G"
                vetor.append(No(aux, estadoAtual))
    return vetor


def sucessoraLargura(estadoAtual,linha):
    aux = expande(estadoAtual, linha)
    for item in aux:
        borda.append(No(item.estado, estadoAtual))
    return borda


def sucessoraProfundidade(estadoAtual,linha):
    aux = expande(estadoAtual, linha)
    for item in aux:
        borda.insert(0,No(item.estado, estadoAtual))
    return borda


def testeDeObjetividade(estadoAtual, combinacoes,borda,tipoBusca):
    if(estadoAtual.getProfundidade() == quant):
        aux = True
        for item in combinacoes:
            if(item.estado == estadoAtual.estado):  # rever
                return False
        if(aux):
            combinacoes.append(estadoAtual)
            if(tipoBusca==1):
                for item in borda:
                    combinacoes.append(item)
            return True



def buscaLocal(estadoInicial, tipoBusca):
    combinacoes = []
    borda = estadoInicial
    linha = 0
    while(linha <= quant):
        estadoAtual = borda[0]
        borda.pop(0)
        visitados.append(estadoAtual)
        count = 0
        for item in estadoAtual.estado:
            if("G" in item):
                count += 1
        linha = count

        if(testeDeObjetividade(estadoAtual, combinacoes,borda,tipoBusca)):
            return combinacoes
        if(tipoBusca == 1):
            borda = sucessoraLargura(estadoAtual,linha)
        else:
            borda = sucessoraProfundidade(estadoAtual, linha)

quant = 8
matriz = No(gerarMatriz(quant), None)
borda = []
borda.append(matriz)
visitados = []
resultado = buscaLocal(borda,1)

print("Quantidade de resultados:",resultado.__len__())

while(resultado[0]!=None):
    print("Profundida:",resultado[0].getProfundidade())
    for item in resultado[0].estado:
        print(item)
    print("")
    resultado[0] = resultado[0].pai
