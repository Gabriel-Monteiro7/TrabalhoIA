class BuscaCustoUniforme:
    def __init__(self):
        self.value ="busca por Custo Uniforme"
    def inserir(self,estado,estadoAtual,borda,quant=None,custo=None,tipoProblema=None,listaVisitados=None,limite = None):
            borda.append(tipoProblema(quant,estado, estadoAtual,custo+estadoAtual.getCusto()))
            #reorganiza a borda de acordo com o custo, para sempre deixa as com o menor custo na cabeça da lista
            borda.sort(key = lambda custo : custo.getCusto())
            return borda
