class BuscaProfundidade:
    def __init__(self):
        self.value ="busca por Profundidade"
    def inserir(self,estado,estadoAtual,borda,quant,custo,tipoProblema=None,tipoProfundidade=None):
        if(type(tipoProfundidade) == list):
            if(not (estado in tipoProfundidade)):
                borda.insert(0,tipoProblema(quant,estado, estadoAtual,custo))
                return borda
        else:
            borda.insert(0,tipoProblema(quant,estado, estadoAtual,custo))
        return borda
        