import random
import numpy
from copy import deepcopy


class AlgoritmoGenetico:
    def __init__(self):
        self.value = "Algoritmo Genético"

    def inserir(self, populacao, quant, tipoProblema, tamanhoPopulacao,selecao):
        novaPopulacao = []

        for item in populacao:
            novaPopulacao.append(item)
            if(novaPopulacao.__len__() == tamanhoPopulacao*0.2):
                break

        crossOver = []
        while(True):
            if(novaPopulacao.__len__() == int(tamanhoPopulacao*0.9)):
                break
            escolhidos = []
            for repeticao in range(selecao*2):
                random.shuffle(populacao)
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
            random.shuffle(populacao)
            for repeticao in range(selecao):
                escolhidos.append(populacao[repeticao])
            escolhidos.sort(key = lambda custo : custo.getCusto())
            escolhidos = escolhidos[0].acharRainha(escolhidos[0],random.randrange(8))
            novaPopulacao.append(escolhidos)
            if(novaPopulacao.__len__() == tamanhoPopulacao):
                break

        return novaPopulacao
