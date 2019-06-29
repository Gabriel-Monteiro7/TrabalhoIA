class BuscaGulosa:
    def __init__(self):
        self.value ="busca Gulosa"
    def inserir(self,estado,estadoAtual,borda,quant=None,custo=None,tipoProblema=None,listaVisitados=None,limite = None):
            if(listaVisitados != None and not estado in listaVisitados):
                borda.append(tipoProblema(quant,estado, estadoAtual,custo))
                borda.sort(key = lambda custo : custo.getCusto())
            #reorganiza a borda de acordo com o custo, para sempre deixa as com o menor custo na cabeça da lista
            return borda