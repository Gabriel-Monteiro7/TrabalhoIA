class BuscaLargura:
    def __init__(self):
        self.value ="busca por Largura"
    def inserir(self,estado,estadoAtual,borda,quant=None,custo=None,tipoProblema=None,tipoProfundidade=None,listaVisitados=None,limite = None):
            borda.append(tipoProblema(quant,estado,estadoAtual,custo+estadoAtual.getCusto()))
            return borda