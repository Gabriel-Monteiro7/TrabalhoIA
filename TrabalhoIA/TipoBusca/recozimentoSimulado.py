import random
import numpy
from copy import deepcopy
class RecozimentoSimulado:
    def __init__(self):
        self.value ="Recozimento simulado"
    def inserir(self,matrizDeEstados,estadoAtual,tipoProblema,quant,sucessoresMaximo,temperatura,coeficiente):   
        retorno = [estadoAtual.estado,estadoAtual.getCusto()]
        sucessores = 0
        random.shuffle(matrizDeEstados)
        for item in matrizDeEstados:
            diferenca = item[1]-retorno[1]
            if(diferenca<=0 or numpy.exp((-diferenca)/temperatura) > random.random()):
                retorno = item
                sucessores+=1
            if(sucessores>=sucessoresMaximo):
                break
            
        return tipoProblema(quant,retorno[0], estadoAtual,retorno[1])
        
        