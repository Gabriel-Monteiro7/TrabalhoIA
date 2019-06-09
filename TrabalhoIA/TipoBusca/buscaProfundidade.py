class BuscaProfundidade:
    def __init__(self):
        self.value ="busca por Profundidade"
    def inserir(self,estadoMatriz,estadoAtual,borda,quant,custo,tipoProblema=None,tipoProfundidade=None):
        if(type(tipoProfundidade) == list):
            if(not (estadoMatriz in tipoProfundidade)):
                borda.insert(0,tipoProblema(quant,estadoMatriz, estadoAtual,custo))
                return borda
        else:
            borda.insert(0,tipoProblema(quant,estadoMatriz, estadoAtual,custo))
        return borda
        