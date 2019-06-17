from No import No
from copy import deepcopy
import random

class Rainha(No):
    def __init__(self,quant,estado = None,pai=None,custo=-1):
        if(estado==None):
            self.estado = gerarMatriz(quant)
        else:
            self.estado = estado
        self.quant = quant
        super().__init__(self.estado,pai,custo+1)

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
        #Aqui ele testa se não existe colisão
        aux = self.testeDeColisao(estadoAtual.estado,coluna,linha)
        for item in aux:
            if('Q' in item):
                return False
        return True

    def testeDeObjetividade(self,estadoAtual,estadoFinal,borda):
        if(estadoAtual.getProfundidade() == self.quant):
            # combinacoes.append(estadoAtual)
            # for item in borda:
            #     combinacoes.append(item)
            return True
        else:
            return False

    def sucessora(self,estadoAtual,borda,tipoBusca,tipoProblema,tipoProfundidade):
        #Aqui ele ve quantas rainhas ja existe e 
        coluna = self.quantidadeRainhas(estadoAtual)
        vetor = []
        for linha in range(self.quant):
            if(estadoAtual.estado[linha][coluna] == "*"):
                if(self.testePosicao(estadoAtual, linha, coluna)):
                    estadoMatriz = deepcopy(estadoAtual.estado)
                    estadoMatriz[linha][coluna] = 'Q'
                    # borda = tipoBusca.inserir(estadoMatriz,estadoAtual,borda,self.quant,linha,tipoProblema,tipoProfundidade)
                    vetor = tipoBusca.inserir(estadoMatriz,estadoAtual,vetor,self.quant,coluna,tipoProblema,tipoProfundidade)
        # if(tipoBusca.value != "busca por Profundidade limitada"):
        random.shuffle(vetor) 
        for item in vetor:
            borda = tipoBusca.inserir(item.estado,estadoAtual,borda,self.quant,coluna,tipoProblema,tipoProfundidade)
        return borda    
    def quantidadeRainhas(self,estadoAtual):
        #Verifica a quantidade de rainhas no tabuleiro
        count=0
        for item in estadoAtual.estado:
            if('Q' in item):
                count += 1
        return count

    def mostraResultado(self,resultado,tempoTotal,estadoInicial,tipoBusca):
        print("")
        print("Estado Inicial")
        for item in estadoInicial.estado:
            print(item)
        print("")
        print("Estado Final")
        for item in resultado.estado:
            print(item)
        print("")
        profundidade = resultado.getProfundidade()
        while(resultado!=None):
            print("Profundida:",resultado.getProfundidade())
            print("Custo:",resultado.getCusto())
            for item in resultado.estado:
                print(item)
            print("")
            resultado = resultado.pai
        print("Profundidade Total:",profundidade)
        print("Tempo total: %.4f" % tempoTotal, "ms. Em minutos: %0.4f mins"%(tempoTotal/60000))

def gerarMatriz(quant):
    matriz = []
    for c in range(quant):
        linha = []
        for l in range(quant):
            linha.append("*")
        matriz.append(linha)
    return matriz
    
    