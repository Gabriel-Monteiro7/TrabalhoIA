import random
class DescidaEncosta:
    def __init__(self):
        self.value ="Descida da encosta"
    def inserir(self,MatrizDeEstados,estadoAtual,tipoProblema,quant,sucessoresMaximo=None,temperatura=None,coeficiente=None):   
        retorno = [estadoAtual.estado,estadoAtual.getCusto()]
        for item in MatrizDeEstados:  
            if(item[1]<retorno[1]):
                retorno = item
        menorValor =[]
        for item in MatrizDeEstados:  
            if(retorno[1]==item[1]):
                menorValor.append(item)
        random.shuffle(menorValor)
        if(menorValor==[]):
            menorValor.append(retorno)
        return tipoProblema(quant,menorValor[0][0], estadoAtual,menorValor[0][1])
        
        