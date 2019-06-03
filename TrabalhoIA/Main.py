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


def teste(matriz, linha, coluna):
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


quant = 8
matriz = No(gerarMatriz(quant), None)
borda = []
bordaMaior = []
borda.append(matriz)
isSalve = True


def expande(valor):
    vetor = []
    for item in valor.filho:
        vetor.insert(0, item)
    return vetor

linha=0
    
while(linha<=quant):
        if(borda==[]):
            borda.append(valor.pai)
        valor = borda[0]
        borda.pop(0)
        for item in valor.estado:
            print(item,linha)
        print("")
        count=0
        if(valor.getProfundidade() == quant):
            aux = True
            for item in bordaMaior:
                if(item.estado == valor.estado):
                    aux = False
            if(aux):
                bordaMaior.append(valor)
                print("%i combinação encontrada" % bordaMaior.__len__())
                for item in borda:
                    bordaMaior.append(item)
                        
                break
        for coluna in range(quant):
            isSalve = True
            if(valor.estado[coluna][linha] == "*"):
                aux = teste(valor.estado, coluna, linha)
                for item in aux:
                    if("G" in item):
                        isSalve = False
                        break
                if(isSalve):
                    aux = deepcopy(valor.estado)
                    aux[coluna][linha] = "G"
                    borda.append(No(aux, valor))
        for item in valor.estado:
            if("G" in item):
                count+=1
        if(count==1+linha):
            linha+=1
        
for item in borda[1].estado:
    print(item)
print("=",bordaMaior.__len__())
while(bordaMaior[10]!=None):
    for item in bordaMaior[10].estado:
        print(item)
    print("")
    bordaMaior[10] = bordaMaior[10].pai

# for col in range(quant):
#     for lin in range(quant):
#         if(matriz[lin][col]==""):
#             isSalve = True
#             for interno in range(quant):
#                 if(matriz[interno][lin] !="" or matriz[col][interno] != "" ):
#                     if(col>lin):# sec prin
#                         if(lin+interno<quant and col+lin<quant and (matriz[lin-interno+1][interno] != "" or matriz[lin+interno][interno] != "")):
#                             isSalve = False
#                             matriz[interno][lin] = "G"
#                     elif(lin>col):
#                         if(interno+col<quant and lin+col<quant and (matriz[lin-interno][interno] != "" or matriz[interno][lin-count+interno] != "")):
#                             isSalve = False
#                             matriz[interno][lin] = "G"
#                     elif(col==lin):
#                         if(col+lin<quant and (matriz[col+lin-interno][interno+1] != "" or matriz[interno][interno] != "")):
#                             isSalve = False
#                             matriz[interno][lin] = "G"


#                     # if(col>lin):
#                     #     if(col - lin == col-1 and matriz[col][interno] != "" and  col + lin == col+1  and matriz[col][interno] != ""):
#                     #         isSalve = False
#                     #         break
#                     # elif(col<lin):
#                     #      if(col + lin == quant and matriz[col][interno] != "" and  lin - col == interno-lin  and matriz[col][interno] != ""):
#                     #         isSalve = False
#                     #         break
#                     # else:
#                     #     if(lin == interno  and matriz[interno][lin] != "" and  lin == interno-lin  and  matriz[col][interno] != ""):
#                     #         isSalve = False
#                     #         break


# print("Elemento na posicao [2,1]")
# print(lin,col,principal)
