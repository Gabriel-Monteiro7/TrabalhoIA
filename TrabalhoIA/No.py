class No:
    def __init__(self, estado=None, pai=None,custo=0):
        self.estado = estado
        self.filho = []
        self.pai = pai
        self.profundidade = 0
        self.custo = custo

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getFilho(self):
        return self.filho

    def setFilho(self, filho):
        self.filho = filho

    def getPai(self):
        return self.pai

    def setPai(self, pai):
        self.pai = pai
    def getProfundidade(self):
        aux = self.pai
        self.profundidade = 0
        while(aux!=None):
            self.profundidade+=1
            aux = aux.pai
        return self.profundidade
    def setCusto(self,custo):
        self.custo = custo
    def getCusto(self):
        return self.custo
    def incrementarCusto(self):
        self.custo+=1