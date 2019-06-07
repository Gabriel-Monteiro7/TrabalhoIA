from no import No
from copy import deepcopy


class Rainha(No):
    def __init__(self,quant,estado = None,pai=None,custo=1):
        if(estado==None):
            self.estado = gerarMatriz(quant)
        else:
            self.estado = estado
        self.quant = quant
        super().__init__(self.estado,pai,custo)

    def testeDeColisao(self,matriz, linha, coluna):
            col = []
            lin = []
            principal = []
            secundaria = []
            linhas = linha
            colunas = coluna
            count = 0
            for item in matriz:
                if(linha > coluna):
                    if((linha-coluna)+count+1 <= self.quant):
                        # achar a principal quando a linha>coluna
                        principal.append(matriz[count+(linha-coluna)][count])
                else:
                    if(coluna-linha+count+1 <= self.quant):
                        # achar a principal quando a coluna>linha
                        principal.append(matriz[count][count+(coluna-linha)])

                if(coluna+linha < self.quant):
                    if(count <= coluna+linha):
                        colunaAux = coluna+linha-count
                        linhaAux = count
                        # achar a secundaria quando a soma da linha e coluna for menor que o grau da matriz
                        secundaria.append(matriz[linhaAux][colunaAux])
                elif(coluna+linha >= self.quant):
                    if(count < (2*self.quant-linha-coluna-1)):
                        colunaAux = linha+coluna-self.quant+count+1
                        linhaAux = self.quant-1-count
                        # achar a secundaria quando a soma da linha e coluna for maior que o grau da matriz
                        secundaria.append(matriz[linhaAux][colunaAux])
                if(count == linhas):
                    lin = item  # achar a linha da posicao
                count += 1
                col.append(item[colunas])  # achar a coluna da posicao
            vetor = [lin, col, principal, secundaria]
            return vetor

    def testePosicao(self,estadoAtual, coluna, linha):
        aux = self.testeDeColisao(estadoAtual.estado,coluna,linha)
        for item in aux:
            if('♕' in item):
                return False
        return True

    def testeDeObjetividade(self,estadoAtual,estadoFinal, combinacoes,borda):
        if(estadoAtual.getProfundidade() == self.quant):
            combinacoes.append(estadoAtual)
            for item in borda:
                combinacoes.append(item)
            return True
        else:
            return False

    def sucessora(self,estadoAtual,borda,tipoBusca,tipoProblema):
        linha = self.quantidadeRainhas(estadoAtual)
        for coluna in range(self.quant):
            if(estadoAtual.estado[coluna][linha] == "*"):
                if(self.testePosicao(estadoAtual, coluna, linha)):
                    aux = deepcopy(estadoAtual.estado)
                    aux[coluna][linha] = '♕'
                    borda = tipoBusca.inserir(aux,estadoAtual,borda,self.quant,linha,tipoProblema)
        return borda
            
    def quantidadeRainhas(self,estadoAtual):
        count=0
        for item in estadoAtual.estado:
            if('♕' in item):
                count += 1
        return count
    def mostraResultado(self,resultado,tempoTotal):
        print("Quantidade de resultados:",resultado.__len__())
        print("CustoTotal:",resultado[0].getCusto())
        while(resultado[0]!=None):
            print("Profundida:",resultado[0].getProfundidade())
            for item in resultado[0].estado:
                print(item)
            print("")
            resultado[0] = resultado[0].pai
        print("Tempo total: %0.1f" % tempoTotal, "ms")

def gerarMatriz(quant):
    matriz = []
    for c in range(quant):
        linha = []
        for l in range(quant):
            linha.append("*")
        matriz.append(linha)
    return matriz
    
    