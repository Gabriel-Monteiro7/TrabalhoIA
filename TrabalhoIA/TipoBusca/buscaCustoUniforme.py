class BuscaCustoUniforme:
    def __init__(self):
        self.value ="busca por Custo Uniforme"
    def inserir(self,estadoMatriz,estadoAtual,borda,quant=None,custo=None,tipoProblema=None,tipoProfundidade=None):
            borda.append(tipoProblema(quant,estadoMatriz, estadoAtual,custo))
            borda.sort(key = lambda custo : custo.getCusto())
            return borda
