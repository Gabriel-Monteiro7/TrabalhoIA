from copy import deepcopy
import time
# 1 == Largura #2 == Profundidade #3 == Custo Uniforme
# ultimo parametro é o tipo de busca se for por profundidade
# [] = se for lista de visitados
# int se for limitado
# Object se for interativa
# Problema(mapaRomenia.opcao(),origem,destino,2,[])

class Agente():
    def __init__(self,quantidade,tipoBusca,tipoProfundidade=None,estadoInicial=None,estadoFinal=None,tipoProblema=None):
        
        self.tipoBusca = tipoBusca()
        self.interacoes=True
        self.limite = None
        self.tipoProfundidade = tipoProfundidade
        
        if(self.tipoBusca.value == "busca por Profundidade"):
            if(type(self.tipoProfundidade) == list):
                self.tipoBusca.value = self.tipoBusca.value+" com lista de visitados"
            elif(type(self.tipoProfundidade)==int):
                self.tipoBusca.value = self.tipoBusca.value+" limitada"
                self.limite=tipoProfundidade-1
            elif(type(self.tipoProfundidade)  == dict):
                self.tipoBusca.value = self.tipoBusca.value+" interativa"
                self.limite=0
        else:
            self.tipoProfundidade = None

        self.tipoProblema = tipoProblema
        self.estadoInicial = estadoInicial
        self.estadoFinal  = estadoFinal
        self.quantidade = quantidade

        buscaAgente(self)

def buscaAgente(self):
    print("Tipo de busca:",self.tipoBusca.value)
    while(self.interacoes):
        print("Resolvendo o problema...")
        combinacoes = [self.estadoInicial]
        borda=[]
        borda.append(self.estadoInicial)
        inicio = time.time()
        while(True):
            if(borda==[]):
                print("Problema atingiu o limite:",self.limite)
                break
            else:
                estadoAtual = borda[0]
                if(type(self.tipoProfundidade)==list):
                    self.tipoProfundidade.append(estadoAtual.estado)
                borda.pop(0)
            combinacoes = [estadoAtual]
            if(estadoAtual.testeDeObjetividade(estadoAtual,self.estadoFinal,combinacoes,borda) or self.limite == estadoAtual.getProfundidade()):
                if(self.tipoBusca.value == "busca por Profundidade interativa" and 
                not estadoAtual.testeDeObjetividade(estadoAtual,self.estadoFinal,combinacoes,borda)):
                    self.limite = 1+estadoAtual.getProfundidade()
                else:
                    self.interacoes = False
                if(self.tipoBusca.value != "busca por Profundidade limitada" or 
                (self.tipoBusca.value == "busca por Profundidade limitada" and self.quantidade == estadoAtual.getProfundidade())):
                    fim = time.time()
                    tempoTotal = (fim - inicio)*1000
                    estadoAtual.mostraResultado(combinacoes,tempoTotal,self.estadoInicial,self.tipoBusca) 
                    break
                else:
                    while(borda[0].getProfundidade()>=self.limite):
                        borda.pop(0)
                        if(borda==[]):
                            break          
            else:
                borda = estadoAtual.sucessora(estadoAtual,borda,self.tipoBusca,self.tipoProblema,self.tipoProfundidade)
        print("")
        
        





