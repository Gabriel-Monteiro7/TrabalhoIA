class BuscaLargura:
    def __init__(self):
        self.value ="busca por Largura"
    def inserir(self,estadoMatriz,estadoAtual,borda,quant=None,custo=None,tipoProblema=None,tipoProfundidade=None):
            borda.append(tipoProblema(quant,estadoMatriz,estadoAtual,custo))
            return borda