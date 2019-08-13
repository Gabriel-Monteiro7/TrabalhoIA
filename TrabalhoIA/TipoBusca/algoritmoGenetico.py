import random
import numpy
from copy import deepcopy


class AlgoritmoGenetico:
    def __init__(self):
        self.value = "Algoritmo Genético"

    def inserir(self, populacao, quant, tipoProblema, tamanhoPopulacao,selecao):
        novaPopulacao = []

        melhor = populacao[0]
        melhores =[]
        for item in populacao:
            if(item.getCusto()==melhor.getCusto() and not item in melhores ):
                melhores.append(item)
            
            # if(melhores.__len__()==tamanhoPopulacao*0.8):
            #     break
        
        while(True):
            indice = random.randrange(melhores.__len__())
            novaPopulacao.append(melhores[indice])
            if(novaPopulacao.__len__() == tamanhoPopulacao*0.1):
                break

        crossOver = []
        while(True):
            if(novaPopulacao.__len__() == int(tamanhoPopulacao*0.9)):
                break
            escolhidos = []
            for repeticao in range(selecao*2):
                random.shuffle(populacao)
                if(not populacao[0] in escolhidos):
                    escolhidos.append(populacao[0])
            escolhidos.sort(key = lambda custo : custo.getCusto())
           
            aux = random.randrange(7)
            estado1 = []
            estado2 = []
            for coluna in range(8):
                linha1 = []
                linha2 = []
                for linha in range(8):
                    if(linha < aux):
                        linha1.append(
                            escolhidos[0].getEstado()[coluna][linha])
                        linha2.append(
                            escolhidos[1].getEstado()[coluna][linha])
                    else:
                        linha1.append(
                            escolhidos[1].getEstado()[coluna][linha])
                        linha2.append(
                            escolhidos[0].getEstado()[coluna][linha])
                estado1.append(linha1)
                estado2.append(linha2)
            crossOver.append(tipoProblema(quant, estado1, None))
            crossOver.append(tipoProblema(quant, estado2, None))
            for iteracao in range(2):
                crossOver[iteracao].setCusto(
                    crossOver[iteracao].testePosicao(crossOver[iteracao].getEstado()))
                novaPopulacao.append(deepcopy(crossOver[iteracao]))

            
        #mutação

        while(True): 
            escolhidos =[]
            for repeticao in range(selecao):
                random.shuffle(populacao)
                escolhidos.append(populacao[0])
            escolhidos.sort(key = lambda custo : custo.getCusto())
            valores = item.sucessora2(escolhidos[0])
            random.shuffle(valores)
            novaPopulacao.append(tipoProblema(quant, valores[0][0], None,valores[0][1]))
            if(novaPopulacao.__len__() == tamanhoPopulacao):
                break
        # for item in melhores:
        #     for item2 in item.getEstado():
        #         print(item2,item.getCusto())
        #     print("")
        return novaPopulacao
