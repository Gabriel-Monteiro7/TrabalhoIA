from no import No
from copy import deepcopy
import random
class Oitopeca(No):
    def __init__(self,quant,estado = None,pai=None,custo=-1):
        if(estado==None):
            self.estado = gerarMatriz(quant)
        else:
            self.estado = estado
        self.quant = quant
        super().__init__(self.estado,pai,custo+1)

    def testeDeObjetividade(self,estadoAtual,estadoFinal, combinacoes,borda):
        if(estadoAtual.getEstado() == estadoFinal.getEstado()):
            combinacoes.append(estadoAtual)
            return True
        else:
            return False

    def sucessora(self,estadoAtual,borda,tipoBusca,tipoProblema,tipoProfundidade):
        movimentoColuna = [self.moverEsquerda,[self.moverEsquerda,self.moverDireita],self.moverDireita]
        movimentoLinha = [self.moverCima,[self.moverCima,self.moverBaixo],self.moverBaixo]
        linhaAux=0
        colunaAux=0
        movimento = []
        for linha in range(self.quant):
            for coluna in range(self.quant):
                if(estadoAtual.estado[linha][coluna] == ''):
                    linhaAux = linha
                    colunaAux = coluna
                    if(type(movimentoLinha[linha]) == list ):
                        movimento.append(movimentoLinha[linha][1])
                        movimento.append(movimentoLinha[linha][0])
                    else:
                        movimento.append(movimentoLinha[linha])
                    if(type(movimentoColuna[coluna]) == list ):
                        movimento.append(movimentoColuna[coluna][0])
                        movimento.append(movimentoColuna[coluna][1])
                    else:
                        movimento.append(movimentoColuna[coluna])
                    break 
            if(movimento.__len__()!=0):
                break 
        random.shuffle(movimento)
        for item in movimento:
            borda = tipoBusca.inserir(item(estadoAtual,linhaAux,colunaAux),estadoAtual,borda,self.quant,estadoAtual.getCusto(),tipoProblema,tipoProfundidade)
        return borda
        
    def mostraResultado(self,resultado,tempoTotal,estadoInicial,tipoBusca):
        resultado = resultado[0]
        print("")
        print("Estado Inicial")
        for item in estadoInicial.getEstado():
            print(item)
        print("")
        print("Estado Final")
        for item in resultado.getEstado():
            print(item)
        print("")
        # while(resultado!=None):
        #     print("Profundida:",resultado.getProfundidade())
        #     print("Custo:",resultado.getCusto())
        #     for item in resultado.getEstado():
        #         print(item)
        #     print("")
        #     resultado = resultado.pai
        print("Profundidade Total:",resultado.getProfundidade())
        print("Custo:",resultado.getCusto())
        print("Tempo total: %.1f" % tempoTotal, "ms. Em minutos: %0.1f mins"%(tempoTotal/60000))
        

    def moverCima(self,estadoAtual,linha,coluna):
        auxEstado = deepcopy(estadoAtual.getEstado())
        auxEstado[linha][coluna] = auxEstado[linha+1][coluna]
        auxEstado[linha+1][coluna] = ''
        return auxEstado

    def moverBaixo(self,estadoAtual,linha,coluna):
        auxEstado = deepcopy(estadoAtual.estado)
        auxEstado[linha][coluna] = auxEstado[linha-1][coluna]
        auxEstado[linha-1][coluna] = ''
        return auxEstado

    def moverEsquerda(self,estadoAtual,linha,coluna):
        auxEstado = deepcopy(estadoAtual.estado)
        auxEstado[linha][coluna] = auxEstado[linha][coluna+1]
        auxEstado[linha][coluna+1] = ''
        return auxEstado

    def moverDireita(self,estadoAtual,linha,coluna):
        auxEstado = deepcopy(estadoAtual.estado)
        auxEstado[linha][coluna] = auxEstado[linha][coluna-1]
        auxEstado[linha][coluna-1] = ''
        return auxEstado   

def gerarMatriz(quant):
    matriz = []
    for c in range(quant):
        linha = []
        for l in range(quant):
            linha.append("*")
        matriz.append(linha)
    return matriz
    

