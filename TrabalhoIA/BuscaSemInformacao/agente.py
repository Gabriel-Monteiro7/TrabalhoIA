from copy import deepcopy
import time
from TipoBusca.buscaProfundidade import BuscaProfundidade
from TipoBusca.buscaLargura import BuscaLargura
# 1 == Largura #2 == Profundidade #3 == Custo Uniforme
# ultimo parametro é o tipo de busca se for por profundidade
# [] = se for lista de visitados
# int se for limitado
# Object se for iterativa
# Problema(mapaRomenia.opcao(),origem,destino,2,[])

class Agente():
    def __init__(self,quantidade,tipoBusca,tipoProfundidade=None,estadoInicial=None,estadoFinal=None,tipoProblema=None):
        
        self.tipoBusca = tipoBusca()
        self.interacoes=True
        self.limite = None
        self.tipoProfundidade = tipoProfundidade
        #Aqui identifica qual tipo de profundidade
        if(self.tipoBusca.value == "busca por Profundidade"):
            if(type(self.tipoProfundidade) == list):
                self.tipoBusca.value = self.tipoBusca.value+" com lista de visitados"
            elif(type(self.tipoProfundidade)==int):
                self.tipoBusca.value = self.tipoBusca.value+" limitada"
                self.limite=tipoProfundidade-1
            elif(type(self.tipoProfundidade)  == dict):
                self.tipoBusca.value = self.tipoBusca.value+" iterativa"
                self.limite=0
        else:
            self.tipoProfundidade = None

        self.tipoProblema = tipoProblema
        self.estadoFinal  = estadoFinal
        self.quantidade = quantidade
        #Aqui pega o estado final e embaralha 20 vezes e faz o resultado ser o estado inicial
        if(estadoInicial==None):
            estadoInicial = [deepcopy(self.estadoFinal)]
            for index in range(20):
                estadoInicial  = estadoInicial[0].sucessora(estadoInicial[0],[],BuscaProfundidade(),self.tipoProblema,None)
            self.estadoInicial = tipoProblema(self.quantidade,estadoInicial[0].getEstado(),None)
        else:
            self.estadoInicial = estadoInicial
        #Inicia o problema
        buscaAgente(self)

def buscaAgente(self):
    print("Tipo de busca:",self.tipoBusca.value)
    print("Resolvendo o problema...")
    inicio = time.time()
    #Aqui vai executar quantas vezes for necessario
    while(self.interacoes):
        # combinacoes = [self.estadoInicial]
        #Inicio a borda
        borda=[]
        borda.append(self.estadoInicial)
        while(True):
            #Aqui ele roda ate achar o resultado, se a borda ficar vazia ele sai
            if(borda==[]):
                if(self.tipoBusca.value == "busca por Profundidade limitada"):
                    print("Problema atingiu o limite:",self.limite)
                break
            else:
                #Senão ele faz o passo a passo do algoritmo, pegar o primeiro da borda
                #se for profundidade com visitados ele add na lista de visitados
                estadoAtual = borda[0]
                if(type(self.tipoProfundidade)==list):
                    self.tipoProfundidade.append(estadoAtual.estado)
                borda.pop(0)
            #Aqui é só pra mostrar os estados se for limitado
            if(self.tipoBusca.value == "busca por Profundidade limitada"):
                for item in estadoAtual.estado:
                    print(item)
                print("")
            # combinacoes = [estadoAtual]
            #TesteObjetivo que verifica o estado ou se ele atingiu o limite
            if(estadoAtual.testeDeObjetividade(estadoAtual,self.estadoFinal,borda) or self.limite == estadoAtual.getProfundidade()):
                #Como interativa vai executar diversas vezes vou incrementando o limite ate achar o valor
                if(self.tipoBusca.value == "busca por Profundidade iterativa" and 
                not estadoAtual.testeDeObjetividade(estadoAtual,self.estadoFinal,borda)):
                    self.limite = 1+estadoAtual.getProfundidade()
                #senão ele achou o valor
                else:
                    self.interacoes = False
                #Aqui ele ja vai chamar o resultado, se limitado for o limite que tiver a reposta ele entra tambem
                fim = time.time()
                tempoTotal = (fim - inicio)*1000
                estadoAtual.mostraResultado(estadoAtual,tempoTotal,self.estadoInicial,self.tipoBusca) 
                print("")
                break
                
                #
                # if(self.tipoBusca.value != "busca por Profundidade limitada" or 
                # (self.tipoBusca.value == "busca por Profundidade limitada" and self.quantidade == estadoAtual.getProfundidade())):
                    
                #Aqui se for limitado ele vai expandir ate achar todos os nós no limite
                # else:
                #     while(borda!=[]):
                #         if(borda[0].getProfundidade()>self.limite):
                #             borda.pop(0)
                #         else:
                #             break 


            #senão achou o valor ele vai expandir a borda        
            else:
                borda = estadoAtual.sucessora(estadoAtual,borda,self.tipoBusca,self.tipoProblema,self.tipoProfundidade)
        
        





