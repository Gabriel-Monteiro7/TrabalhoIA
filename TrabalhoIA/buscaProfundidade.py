class BuscaProfundidade:
    def inserir(estadoMatriz,estadoAtual,borda,quant,linha,tipoProblema=None,tipoProfundidade=None):
        if(type(tipoProfundidade) == list):
            if(not (estadoMatriz in tipoProfundidade)):
                borda.append(tipoProblema(quant,estadoMatriz, estadoAtual,1+linha))
                return borda
        return borda
        