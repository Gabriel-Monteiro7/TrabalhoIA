class BuscaCustoUniforme:
    def __init__(self):
        self.value ="busca por Custo Uniforme"
    def inserir(self,estado,estadoAtual,borda,quant=None,custo=None,tipoProblema=None,tipoProfundidade=None):
            borda.append(tipoProblema(quant,estado, estadoAtual,custo))
            borda.sort(key = lambda custo : custo.getCusto())
            return borda
