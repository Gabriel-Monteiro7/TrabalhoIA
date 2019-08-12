import random
import numpy
from copy import deepcopy


class AlgoritmoGenetico:
    def __init__(self):
        self.value = "Algoritmo Genético"

    def inserir(self, populacao, quant, tipoProblema, tamanhoPopulacao):
        custoMaximo = quant*(quant-1)/2
        novaPopulacao = []
        
        while(True):
            random.shuffle(populacao)
            cadidato1 = deepcopy(populacao[0])
            random.shuffle(populacao)
            cadidato2 = deepcopy(populacao[0])
            if(cadidato1.getCusto()>cadidato2.getCusto()):
                novaPopulacao.append(cadidato2)
            else:
                novaPopulacao.append(cadidato1)
            if(novaPopulacao.__len__() == tamanhoPopulacao*0.5):
                break
            # if(melhores.__len__()==tamanhoPopulacao*0.8):
            #     break
       
        crossOver = []
        Aux = random.randrange(8)
        for repeticao in range(int(tamanhoPopulacao*0.2-1)):
            estado1 = []
            estado2 = []
            
            for coluna in range(8):
                linha1 = []
                linha2 = []
                for linha in range(8):
                    if(linha < Aux):
                        linha1.append(
                            novaPopulacao[repeticao].getEstado()[coluna][linha])
                        linha2.append(
                            novaPopulacao[repeticao+1].getEstado()[coluna][linha])
                    else:
                        linha1.append(
                            novaPopulacao[repeticao+1].getEstado()[coluna][linha])
                        linha2.append(
                            novaPopulacao[repeticao].getEstado()[coluna][linha])
                estado1.append(linha1)
                estado2.append(linha2)
            crossOver.append(tipoProblema(quant, estado1, None))
            crossOver.append(tipoProblema(quant, estado2, None))
        for iteracao in range(int(tamanhoPopulacao*0.2)):
            crossOver[iteracao].setCusto(
                crossOver[iteracao].testePosicao(crossOver[iteracao].getEstado()))
            novaPopulacao.append(deepcopy(crossOver[iteracao]))
        #mutação

        for item in novaPopulacao: 
            valores = item.sucessora2(item)
            random.shuffle(valores)
            novaPopulacao.append(tipoProblema(quant, valores[0][0], None,valores[0][1]))
            if(novaPopulacao.__len__() == tamanhoPopulacao):
                break
        # for item in melhores:
        #     for item2 in item.getEstado():
        #         print(item2,item.getCusto())
        #     print("")
        return novaPopulacao
