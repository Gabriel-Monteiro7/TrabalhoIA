from no import No
from copy import deepcopy
import random
class Oitopeca(No):
    def __init__(self,quant,estado = None,pai=None,custo=1):
        if(estado==None):
            self.estado = gerarMatriz(quant)
        else:
            self.estado = estado
        self.quant = quant
        super().__init__(self.estado,pai,custo)

    def testeDeObjetividade(self,estadoAtual,estadoFinal, combinacoes,borda):
        if(estadoAtual.estado == estadoFinal.estado):
            combinacoes.append(estadoAtual)
            return True
        else:
            return False

    def sucessora(self,estadoAtual,borda,tipoBusca,tipoProblema,tipoProfundidade):
        movimentoColuna = [self.moverEsquerda,[self.moverEsquerda,self.moverDireita],self.moverDireita]
        movimentoLinha = [self.moverCima,[self.moverCima,self.moverBaixo],self.moverBaixo]
        for linha in range(self.quant):
            for coluna in range(self.quant):
                if(estadoAtual.estado[linha][coluna] == ''):
                    movimento = []
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
                    random.shuffle(movimento)
                    for item in movimento:
                        borda = tipoBusca.inserir(item(estadoAtual,linha,coluna),estadoAtual,borda,self.quant,linha,tipoProblema,tipoProfundidade)
                    return borda
        
            
    def mostraResultado(self,resultado,tempoTotal,estadoInicial):
        resultado = resultado[0]
        print("Estado Inicial")
        for item in estadoInicial.estado:
            print(item)
        print("")
        print("Estado Final")
        for item in resultado.estado:
            print(item)
        print("")
        while(resultado!=None):
            print("Profundida:",resultado.getProfundidade())
            for item in resultado.estado:
                print(item)
            print("")
            resultado = resultado.pai
        print("Tempo total: %0.1f" % tempoTotal, "ms")
        

    def moverCima(self,estadoAtual,linha,coluna):
        auxEstado = deepcopy(estadoAtual.estado)
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
    

