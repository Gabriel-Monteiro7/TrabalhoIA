from copy import deepcopy
import time

class AgenteMapa():
    def __init__(self,tipoBusca,tipoProfundidade=None,estadoInicial=None,estadoFinal=None,tipoProblema=None):
        
        self.tipoBusca = tipoBusca()
        self.iteracoes=True
        self.tipoProfundidade = tipoProfundidade
        #Aqui identifica qual tipo de profundidade
        if(self.tipoBusca.value == "busca por Profundidade"):
            if(type(self.tipoProfundidade) == list):
                self.tipoBusca.value = self.tipoBusca.value+" com lista de visitados"
            elif(type(self.tipoProfundidade)==int):
                self.tipoBusca.value = self.tipoBusca.value+" limitada"
                self.tipoProfundidade-=1
            elif(type(self.tipoProfundidade)  == dict):
                self.tipoBusca.value = self.tipoBusca.value+" iterativa"
                self.tipoProfundidade=0
            #Se for iteratica ou limitada ele seta no tipo problema o limite que sera checado na busca em si
        else:
            self.tipoProfundidade = None
        self.tipoProblema = tipoProblema
        self.estadoFinal  = estadoFinal
        
        self.estadoInicial = estadoInicial
        #Inicia o problema
        buscaAgente(self)

def buscaAgente(self):
    print("Tipo de busca:",self.tipoBusca.value)
    print("Resolvendo o problema...")
    inicio = time.time()
    #Aqui vai executar quantas vezes for necessario
    while(self.iteracoes):
        # combinacoes = [self.estadoInicial]
        #Inicio a borda
        borda=[]
        borda.append(self.estadoInicial)
        aux = borda[0]
        passos =0
        while(True):
            #Aqui ele roda ate achar o resultado, se a borda ficar vazia ou atingir uma quantidade de passos
            #Se for vazia ele volta um nivel(profundidade), é mais aplicado ao profundidade iterativo
            if(borda ==[] or passos==500000):
                if(borda != []):
                    print("Valor não encontrado")
                    print("Limite na quantidade de passos:",passos)
                    self.iteracoes = False
                    break
                else:
                    borda = [aux]
            else:
                #Senão ele faz o passo a passo do algoritmo, pegar o primeiro da borda
                #se for profundidade com visitados ele add na lista de visitados
                estadoAtual = borda[0]
                if(type(self.tipoProfundidade)==list):
                    self.tipoProfundidade.append(estadoAtual.estado)
                borda.pop(0)
            print("Quantidade de passos:", passos)
            print("Estado atual:", estadoAtual.getEstado())
            print("")
            passos+=1
            #Aqui é só pra mostrar os estados se for limitado   
            # combinacoes = [estadoAtual]
            #TesteObjetivo que verifica o estado ou se ele atingiu o limite.
            #Se ele for o iterativo ele incrementa o limite(tipoProblema), senao ele verifica
            #se ele atingiu o limite por ser a profundidade limitada, se for ele para, senao ele
            #quer dizer que o valor foi encontrado, ele printa o caminho e diz que achou o caminho.
            if(estadoAtual.testeDeObjetividade(estadoAtual,self.estadoFinal,borda) 
            or (self.tipoProfundidade == estadoAtual.getProfundidade() and borda ==[])):
                #Como interativa vai executar diversas vezes vou incrementando o limite ate achar o valor
                if(self.tipoBusca.value == "busca por Profundidade iterativa" and 
                not estadoAtual.testeDeObjetividade(estadoAtual,self.estadoFinal,borda)):
                    print("Problema atingiu o limite:",self.tipoProfundidade)
                    aux = estadoAtual
                    self.tipoProfundidade = 1+estadoAtual.getProfundidade()
                    break
                #senão ele achou o valor
                else:
                    if(self.tipoBusca.value == "busca por Profundidade limitada" and not
                    estadoAtual.testeDeObjetividade(estadoAtual,self.estadoFinal,borda)):
                        print("Valor não encontrado")
                        print("Problema atingiu o limite:",self.tipoProfundidade)
                    else:
                        print("Valor encontrado")
                    fim = time.time()
                    tempoTotal = (fim - inicio)*1000
                    estadoAtual.mostraResultado(estadoAtual,tempoTotal,self.estadoInicial,self.tipoBusca,passos) 
                    print("")
                    self.iteracoes = False
                    break
            #senão achou o valor ele vai expandir o estado atual e add na borda de acordo com sua busca
            else:
                borda = estadoAtual.sucessora(estadoAtual,borda,self.tipoBusca,self.tipoProblema,self.tipoProfundidade)
        
        





