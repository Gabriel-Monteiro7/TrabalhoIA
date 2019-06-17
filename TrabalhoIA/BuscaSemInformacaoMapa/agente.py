from copy import deepcopy
import time



class AgenteMapa():
    def __init__(self,tipoBusca, tipoProfundidade=None, estadoInicial=None, estadoFinal=None, tipoProblema=None):

        self.tipoBusca = tipoBusca()
        self.interacoes = True
        self.limite = None
        self.tipoProfundidade = tipoProfundidade

        if(self.tipoBusca.value == "busca por Profundidade"):
            if(type(self.tipoProfundidade) == list):
                self.tipoBusca.value = self.tipoBusca.value+" com lista de visitados"
            elif(type(self.tipoProfundidade) == int):
                self.tipoBusca.value = self.tipoBusca.value+" limitada"
                self.limite = tipoProfundidade-1
            elif(type(self.tipoProfundidade) == dict):
                self.tipoBusca.value = self.tipoBusca.value+" iterativa"
                self.limite = 0
        else:
            self.tipoProfundidade = None

        self.tipoProblema = tipoProblema
        self.estadoInicial = estadoInicial
        self.estadoFinal = estadoFinal

        buscaAgente(self)


def buscaAgente(self):
    print("Tipo de busca:", self.tipoBusca.value)
    print("Resolvendo o problema...")
    inicio = time.time()
    # Aqui vai executar quantas vezes for necessario
    while(self.interacoes):
        # combinacoes = [self.estadoInicial]
        # Inicio a borda
        borda = []
        borda.append(self.estadoInicial)
        passos=0
        while(True):
            # Aqui ele roda ate achar o resultado, se a borda ficar vazia ele sai
            if(borda == []):
                break
            else:
                # Senão ele faz o passo a passo do algoritmo, pegar o primeiro da borda
                # se for profundidade com visitados ele add na lista de visitados
                estadoAtual = borda[0]
                if(type(self.tipoProfundidade) == list):
                    self.tipoProfundidade.append(estadoAtual.estado)
                borda.pop(0)
            passos += 1
            print("Quantidade de passos:", passos)
            print("Estado atual:", estadoAtual.getEstado())
            print("")
            # Aqui é só pra mostrar os estados se for limitado
            # combinacoes = [estadoAtual]
            # TesteObjetivo que verifica o estado ou se ele atingiu o limite.
            # Se o limite for na limitada ele ja para, se for na iterativa ele garante se ja chegou no
            # valor desejado
            if(estadoAtual.testeDeObjetividade(estadoAtual, self.estadoFinal, borda)
               or (self.limite == estadoAtual.getProfundidade() and borda == [])
               or (self.limite == estadoAtual.getProfundidade() and (type(self.tipoProfundidade) == int))):
                # Como interativa vai executar diversas vezes vou incrementando o limite ate achar o valor
                if(self.tipoBusca.value == "busca por Profundidade iterativa" and
                   not estadoAtual.testeDeObjetividade(estadoAtual, self.estadoFinal, borda)):
                    print("Problema atingiu o limite:", self.limite)
                    print("")
                    self.limite = 1+estadoAtual.getProfundidade()
                    break
                # senão ele achou o valor
                else:
                    if((type(self.tipoProfundidade) == int) and not
                       estadoAtual.testeDeObjetividade(estadoAtual, self.estadoFinal, borda)):
                        print("Problema atingiu o limite:", self.limite)
                    else:
                        fim = time.time()
                        tempoTotal = (fim - inicio)*1000
                        estadoAtual.mostraResultado(
                            estadoAtual, tempoTotal, self.estadoInicial, self.tipoBusca,passos)
                        print("")
                    self.interacoes = False
                    break
            # senão achou o valor ele vai expandir a borda
            elif(self.limite != estadoAtual.getProfundidade()):
                borda = estadoAtual.sucessora(
                    estadoAtual, borda, self.tipoBusca, self.tipoProblema, self.tipoProfundidade)
