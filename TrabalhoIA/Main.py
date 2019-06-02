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
#1 == Largura #2 == Profundidade #3 == Custo Uniforme
#ultimo parametro é o tipo de busca se for por profundidade 
#[] = se for lista de visitados 
#int se for limitado
#Object se for interativa
# Problema(mapaRomenia.opcao(),origem,destino,2,[])

def gerarMatriz(quant):
    matriz =[]
    for c in range(quant):
        linha = []
        for l in range(quant):
            linha.append("*")
        matriz.append(linha)
    
    return matriz
def teste(matriz,linha,coluna):
    col=[]
    lin=[]
    principal=[]
    secundaria =[]
    linhas=linha
    colunas=coluna
    count =0
    for item in matriz:
        if(linha>coluna):
            if((linha-coluna)+count+1<=quant):
                principal.append(matriz[count+(linha-coluna)][count]) #achar a principal quando a linha>coluna
        else:
            if(coluna-linha+count+1<=quant):
                principal.append(matriz[count][count+(coluna-linha)]) #achar a principal quando a coluna>linha

        if(coluna+linha<quant):
            if(count<=coluna+linha):
                colunaAux = coluna+linha-count
                linhaAux = count
                secundaria.append(matriz[linhaAux][colunaAux]) #achar a secundaria quando a soma da linha e coluna for menor que o grau da matriz
        elif(coluna+linha>=quant):
            if(count<(2*quant-linha-coluna-1)):
                colunaAux = linha+coluna-quant+count+1
                linhaAux = quant-1-count
                secundaria.append(matriz[linhaAux][colunaAux])#achar a secundaria quando a soma da linha e coluna for maior que o grau da matriz
        if(count==linhas):
            lin = item #achar a linha da posicao
        count+=1
        col.append(item[colunas]) #achar a coluna da posicao
    vetor = [lin,col,principal,secundaria]
    return vetor

quant = 5
matriz = No(gerarMatriz(quant),None)
vetor = [0,4,7,5,2,6,1,3]
count=0
borda = []
borda.append(matriz)
while(True):
    if(borda == []):
        print("")
        break
    else:
        aux =0
        for item in borda[0].estado:
            if("G" in item):
                aux+=1
        if(aux==quant):
            break
        else:
            for coluna in range(quant):
                for linha in range(quant):
                    isSalve = True
                    if(matriz.estado[linha][coluna]=="*"):
                        aux = teste(matriz.estado,linha,coluna)
                        for item in aux:
                            if("G" in item):
                                isSalve=False
                                break
                        if(isSalve):
                            aux = deepcopy(matriz)
                            aux.estado[linha][coluna] = "G"
                            borda[0].filho.append(No(aux,borda[0]))
                            matriz.estado[linha][coluna] = "G"
                            break
            borda.pop(0)


for item in matriz.estado:
    print(item)


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