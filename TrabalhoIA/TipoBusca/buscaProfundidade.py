class BuscaProfundidade:
    def __init__(self):
        self.value ="busca por Profundidade"
    def inserir(self,estado,estadoAtual,borda,quant,custo,tipoProblema=None,listaVisitados=None,limite = None):
        #List ade visitados
        if(listaVisitados != None and (estado in listaVisitados)):
            return borda
        #Se tiver atingindo o limite(limitada ou iterativa)
        elif(limite==estadoAtual.getProfundidade()):
            return borda
        borda.insert(0,tipoProblema(quant,estado, estadoAtual,custo))
        return borda
        