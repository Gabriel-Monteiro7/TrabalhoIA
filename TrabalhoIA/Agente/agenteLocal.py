from copy import deepcopy
import time
import random
class AgenteLocal():
    def __init__(self,quantidade,tipoBusca,estadoInicial=None,tipoProblema=None,sucessoresMaximo=None,temperaturaInicial=None,coeficiente = None):
        
        self.tipoBusca = tipoBusca()
        self.tipoProblema = tipoProblema
        self.quantidade = quantidade
        self.estadoInicial = estadoInicial
        self.sucessoresMaximo = sucessoresMaximo
        self.temperaturaInicial = temperaturaInicial
        self.coeficiente = coeficiente
        #Inicia o problema
        buscaAgenteLocal(self)

def buscaAgenteLocal(self):
    print("Tipo de busca:",self.tipoBusca.value)
    print("Resolvendo o problema...")
    inicio = time.time()
    #Aqui vai executar quantas vezes for necessario
    passos = 0
    estado = self.estadoInicial
    while(True):

        if(estado.testeDeObjetividade() or passos == 1000):
            fim = time.time()
            tempoTotal = (fim - inicio)*1000
            mostraResultado(self,estado,tempoTotal,self.estadoInicial,passos)
            if(passos == 1000):
                print("Entrou num minimo local")
            break
        else:
            novoEstado = estado.sucessora(estado,self.tipoBusca,self.tipoProblema,self.sucessoresMaximo,self.temperaturaInicial,self.coeficiente);    
            if(self.temperaturaInicial!=None):
                self.temperaturaInicial = self.temperaturaInicial*self.coeficiente     
            estado = novoEstado
        passos+=1
def mostraResultado(self,resultado,tempoTotal,estadoInicial,passos):
        resultadoAux = resultado
        print("Estado Inicial")
        for item in estadoInicial.getEstado():
            print(item)
        print("")
        print("Estado Final")
        for item in resultadoAux.getEstado():
            print(item)
        print("")
        print("Profundidade Total:",resultadoAux.getProfundidade())
        print("Custo:",resultadoAux.getCusto())
        print("Tempo total: %.4f" % tempoTotal, "ms. Em minutos: %0.4f mins"%(tempoTotal/60000))     