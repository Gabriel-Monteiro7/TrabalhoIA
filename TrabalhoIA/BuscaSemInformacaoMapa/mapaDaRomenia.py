from no import No
from collections import ChainMap
import random
# -- coding: utf-8 --


class MapaDaRomenia(No):

    def __init__(self,quant=None,estado = None,pai=None,custo=0):

        self.Arad = No("Arad", None)

        insert(self.Arad, No("Sibiu", self.Arad, 140))
        insert(self.Arad, No("Zerind", self.Arad, 75))
        insert(self.Arad, No("Timisoara", self.Arad, 118))

        self.Timisoara = No("Timisoara", None)

        insert(self.Timisoara, No("Arad", self.Timisoara, 118))
        insert(self.Timisoara, No("Lugoj", self.Timisoara, 111))

        self.Zerind = No("Zerind", None)

        insert(self.Zerind, No("Arad", self.Zerind, 75))
        insert(self.Zerind, No("Oradea", self.Zerind, 71))

        self.Oradea = No("Oradea", None)

        insert(self.Oradea, No("Zerind", self.Oradea, 71))
        insert(self.Oradea, No("Sibiu", self.Oradea, 151))

        self.Lugoj = No("Lugoj", None)

        insert(self.Lugoj, No("Mehadia", self.Lugoj, 70))
        insert(self.Lugoj, No("Timisoara", self.Lugoj, 111))

        self.Mehadia = No("Mehadia", None)

        insert(self.Mehadia, No("Dobreta", self.Mehadia, 75))
        insert(self.Mehadia, No("Lugoj", self.Mehadia, 70))

        self.Dobreta = No("Dobreta", None)

        insert(self.Dobreta, No("Craiova", self.Dobreta, 120))
        insert(self.Dobreta, No("Mehadia", self.Dobreta, 75))

        self.Craiova = No("Craiova", None)

        insert(self.Craiova, No("Dobreta", self.Craiova, 120))
        insert(self.Craiova, No("Rimnicu Vilcea", self.Craiova, 146))
        insert(self.Craiova, No("Pitesti", self.Craiova, 138))

        self.Sibiu = No("Sibiu", None)

        insert(self.Sibiu, No("Fagaras", self.Sibiu, 99))
        insert(self.Sibiu, No("Rimnicu Vilcea", self.Sibiu, 80))
        insert(self.Sibiu, No("Arad", self.Sibiu, 140))
        insert(self.Sibiu, No("Oradea", self.Sibiu, 151))

        self.Fagaras = No("Fagaras", None)

        insert(self.Fagaras, No("Bucharest", self.Fagaras, 211))
        insert(self.Fagaras, No("Sibiu", self.Fagaras, 99))

        self.Rv = No("Rimnicu Vilcea", None)

        insert(self.Rv, No("Pitesti", self.Rv, 97))
        insert(self.Rv, No("Sibiu", self.Rv, 80))
        insert(self.Rv, No("Craiova", self.Rv, 146))

        self.Pitesti = No("Pitesti", None)

        insert(self.Pitesti, No("Rimnicu Vilcea", self.Pitesti, 97))
        insert(self.Pitesti, No("Bucharest", self.Pitesti, 101))
        insert(self.Pitesti, No("Craiova", self.Pitesti, 138))

        self.Bucharest = No("Bucharest", None)

        insert(self.Bucharest, No("Urziceni", self.Bucharest, 85))
        insert(self.Bucharest, No("Giurgia", self.Bucharest, 90))
        insert(self.Bucharest, No("Pitesti", self.Bucharest, 101))
        insert(self.Bucharest, No("Fagaras", self.Bucharest, 211))

        self.Giurgiu = No("Giurgia", None)

        insert(self.Giurgiu, No("Bucharest", self.Giurgiu, 90))

        self.Urziceni = No("Urziceni", None)

        insert(self.Urziceni, No("Vaslui", self.Urziceni, 142))
        insert(self.Urziceni, No("Bucharest", self.Urziceni, 85))
        insert(self.Urziceni, No("Hirsova", self.Urziceni, 98))

        self.Hirsova = No("Hirsova", None)

        insert(self.Hirsova, No("Urziceni", self.Hirsova, 98))
        insert(self.Hirsova, No("Eforie", self.Hirsova, 86))

        self.Eforie = No("Eforie", None)

        insert(self.Eforie, No("Hirsova", self.Eforie, 86))

        self.Vaslui = No("Vaslui", None)

        insert(self.Vaslui, No("Iasi", self.Vaslui, 92))
        insert(self.Vaslui, No("Urziceni", self.Vaslui, 142))

        self.Iasi = No("Iasi", None)

        insert(self.Iasi, No("Neamt", self.Iasi, 87))
        insert(self.Iasi, No("Vaslui", self.Iasi, 92))

        self.Neamt = No("Neamt", None)

        insert(self.Neamt, No("Iasi", self.Neamt, 87))

        self.vetorTotal = ChainMap({"Arad": self.Arad}, {"Sibiu": self.Sibiu}, {"Fagaras": self.Fagaras},
                            {"Bucharest": self.Bucharest}, {
            "Rimnicu Vilcea": self.Rv}, {"Pitesti": self.Pitesti},
            {"Zerind": self.Zerind}, {"Oradea": self.Oradea}, {"Timisoara": self.Timisoara}, {"Lugoj": self.Lugoj}, {"Mehadia": self.Mehadia}, {
            "Dobreta": self.Dobreta}, {"Craiova": self.Craiova}, {"Giurgiu": self.Giurgiu}, {"Urziceni": self.Urziceni},
            {"Hirsova": self.Hirsova}, {"Eforie": self.Eforie}, {
            "Vaslui": self.Vaslui}, {"Iasi": self.Iasi}, {"Neamt": self.Neamt}
        )
        if(estado!=None):
            if(pai!=None):
                custoPai=0
                for item in self.vetorTotal[estado].filho:
                    if(item.getEstado() == pai.getEstado()):
                        custoPai = item.getCusto()
                super().__init__(self.vetorTotal[estado].getEstado(),pai,custo+custoPai)
            else:
                super().__init__(self.vetorTotal[estado].getEstado(),pai,custo)
        else:
            super().__init__()


    def mostraResultado(self,resultado,tempoTotal,estadoInicial,tipoBusca):
        resultado = resultado[0]
        print("")
        print("Estado Inicial")
        print(estadoInicial.getEstado())
        print("")
        print("Estado Final")
        print(resultado.getEstado())
        print("")
        print("Caminho é:", end='')
        estadoAtual = resultado
        caminho = []
        while(resultado!=None):
            caminho.append(resultado)
            resultado = resultado.pai
        caminho.reverse()
        for item in caminho:
            print(" -->", item.getEstado(), end='')
        print("")
        print("Custo Total:",estadoAtual.getCusto())
        print("Profundidade Total:",estadoAtual.getProfundidade())
        print("Tempo total: %.1f" % tempoTotal, "ms. Em minutos: %0.1f mins"%(tempoTotal/60000))
        
    def sucessora(self,estadoAtual,borda,tipoBusca,tipoProblema,tipoProfundidade):
        aux = expande(self.vetorTotal[estadoAtual.getEstado()])
        random.shuffle(aux)
        for item in aux:
            borda = tipoBusca.inserir(item.getEstado(),estadoAtual,borda,None,estadoAtual.getCusto(),tipoProblema,tipoProfundidade)
        return borda


    def testeDeObjetividade(self,estadoAtual,estadoFinal, combinacoes,borda):
        if(estadoAtual.getEstado() == estadoFinal.getEstado()):
            combinacoes.append(estadoAtual)
            return True
        else:
            return False

def insert(noExistente, no):
        noExistente.filho.append(no)


def expande(estadoAtual):
        vetor = []
        for item in estadoAtual.filho:
            vetor.insert(0, item)
        return vetor