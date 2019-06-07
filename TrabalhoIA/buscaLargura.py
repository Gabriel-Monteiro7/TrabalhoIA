class BuscaLargura:
    def inserir(estadoMatriz,estadoAtual,borda,quant,linha,tipoProblema=None):
        if(type(tipoProblema) == list):
            save = True
            print(estadoMatriz == tipoProblema[0])
            for item in tipoProblema:
                if(item==estadoMatriz):
                    print("oi")
                    save = False
            if(save):
                borda.append(tipoProblema(quant,estadoMatriz, estadoAtual,1+linha))
                return borda
        return borda