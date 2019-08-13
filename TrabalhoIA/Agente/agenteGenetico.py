from copy import deepcopy
import time
import random
class AgenteGenetico():
    def __init__(self,quantidade,tipoBusca,estadoInicial=None,tipoProblema=None,tamanhoPopulacao=None,selecao=None):
        
        self.tipoBusca = tipoBusca()
        self.tipoProblema = tipoProblema
        self.quantidade = quantidade
        self.estadoInicial = estadoInicial
        self.tamanhoPopulacao = tamanhoPopulacao
        self.selecao = selecao
        #Inicia o problema
        buscaAgenteLocal(self)

def buscaAgenteLocal(self):
    estadoInicial = deepcopy(self.estadoInicial)
    estado=[]
    for item in range(self.tamanhoPopulacao):
        valores = estadoInicial.sucessora2(estadoInicial)
        random.shuffle(valores)
        estado.append(self.tipoProblema(self.quantidade, valores[0][0], None,valores[0][1]))
    print("Tipo de busca:",self.tipoBusca.value)
    print("Resolvendo o problema...")
    inicio = time.time()
    #Aqui vai executar quantas vezes for necessario
    passos = 0
    while(True):
        estado.sort(key = lambda custo : custo.getCusto())
        menor = estado[0]
        # for item in menor.getEstado():
        #     print(item,menor.getCusto())
        # print("")
        
        if(menor.testeDeObjetividade() or passos == 5000):
            fim = time.time()
            tempoTotal = (fim - inicio)*1000
            mostraResultado(self,menor,tempoTotal,self.estadoInicial,passos)
            if(passos == 5000):
                print("Atingiu o Limite")
            break
        else:
            estado = self.tipoBusca.inserir(estado,self.quantidade,self.tipoProblema,self.tamanhoPopulacao,self.selecao);   
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