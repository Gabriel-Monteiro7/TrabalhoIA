import random
import numpy
from copy import deepcopy


class AlgoritmoGenetico:
    def __init__(self):
        self.value = "Algoritmo Genetico"

    def inserir(self, populacao, quant, tipoProblema, tamanhoPopulacao):
        melhores = []
        custoConflito = 0
        custoMaximo = quant*(quant-1)/2
        novaPopulacao = []

        for item in populacao:
            melhores.append(deepcopy(item))
            custoConflito += custoMaximo-item.getCusto()
            random.shuffle(populacao)
            if(melhores.__len__() == 4):
                break
            # if(melhores.__len__()==tamanhoPopulacao*0.8):
            #     break
        melhores.sort(key=lambda custo: custo.getCusto())
        porcentagem = []
        acumuloCusto = 0
        for item in range(4):
            acumuloCusto += (custoMaximo - melhores[item].getCusto())/custoConflito
            porcentagem.append(acumuloCusto)

        for item in range(int(tamanhoPopulacao*0.8)):
            valor = random.random()
            if(valor >= 0 and valor <= porcentagem[0]):
                novaPopulacao.append(melhores[0])
            elif (valor > porcentagem[0] and valor <= porcentagem[1]):
                novaPopulacao.append(melhores[1])
            elif (valor > porcentagem[1] and valor <= porcentagem[2]):
                novaPopulacao.append(melhores[2])
            else:
                novaPopulacao.append(melhores[3])
        
        crossOver = []
        for repeticao in range(int(tamanhoPopulacao*0.1-1)):
            estado1 = []
            estado2 = []
            for coluna in range(8):
                linha1 = []
                linha2 = []
                for linha in range(8):
                    if(linha < 4):
                        linha1.append(
                            melhores[repeticao].getEstado()[coluna][linha])
                        linha2.append(
                            melhores[repeticao+1].getEstado()[coluna][linha])
                    else:
                        linha1.append(
                            melhores[repeticao+1].getEstado()[coluna][linha])
                        linha2.append(
                            melhores[repeticao].getEstado()[coluna][linha])
                estado1.append(linha1)
                estado2.append(linha2)
            crossOver.append(tipoProblema(quant, estado1, None))
            crossOver.append(tipoProblema(quant, estado2, None))
        random.shuffle(crossOver)
        for iteracao in range(int(tamanhoPopulacao*0.1)):
            crossOver[iteracao].setCusto(
                crossOver[iteracao].testePosicao(crossOver[iteracao].getEstado()))
            novaPopulacao.append(deepcopy(crossOver[iteracao]))
        #mutação

        for item in melhores: 
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
