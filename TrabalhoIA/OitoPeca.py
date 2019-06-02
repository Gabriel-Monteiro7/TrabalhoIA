from No import No
from collections import ChainMap
class OitoPeca:
    def __init__(self, quant):
        self.quant = quant
        
    

        

def gerarMatriz(quant):
    matriz =[]
    for l in range(quant):
        matriz.append(["*"]*quant)
    return matriz

def compararMatriz(matrizA,matrizB):
    if(matrizA==matrizB):
        return True
    else:
        return False
