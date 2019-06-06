from rainhas import Rainha
class BuscaLargura:
    def inserir(estadoMatriz,estadoAtual,borda,quant,linha,tipoProblema=None):
        borda.append(tipoProblema(quant,estadoMatriz, estadoAtual,1+linha))
        return borda