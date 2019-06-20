class BuscaProfundidade:
    def __init__(self):
        self.value ="busca por Profundidade"
    def inserir(self,estado,estadoAtual,borda,quant,custo,tipoProblema=None,tipoProfundidade=None):
        #List ade visitados
        if(type(tipoProfundidade) == list):
            if(not (estado in tipoProfundidade)):
                borda.insert(0,tipoProblema(quant,estado, estadoAtual,custo))
                return borda
        #Se tiver atingindo o limite(limitada ou iterativa)
        elif(type(tipoProfundidade) == int and tipoProfundidade==estadoAtual.getProfundidade()):
            return borda
        borda.insert(0,tipoProblema(quant,estado, estadoAtual,custo))
        return borda
        