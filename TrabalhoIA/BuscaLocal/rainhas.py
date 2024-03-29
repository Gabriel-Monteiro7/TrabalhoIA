from No import No
from copy import deepcopy
import random

class RainhaLocal(No):
    def __init__(self,quant,estado = None,pai=None,custo=1000):
        self.estado = estado
        self.quant = quant
        if(estado==None):
            self.estado = gerarMatriz(quant)
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

    def testePosicao(self,estadoAtual,quant=None):
        if(quant!=None):
            self.quant = quant
        #Aqui ele testa se não existe colisão
        colisaoTotal=0
        auxEstado = deepcopy(estadoAtual)
        for linha in range(self.quant):
            for coluna in range(self.quant):
                if(auxEstado[coluna][linha]=="Q"):
                    aux = self.testeDeColisao(auxEstado,coluna,linha)
                    for item in aux:
                        colisoes = -1
                        for item2 in item:
                            if(item2 == "Q"):
                                colisoes+=1
                        colisaoTotal+=colisoes
                    auxEstado[coluna][linha] = "*"
        return colisaoTotal

    def acharRainha(self,estadoAtual,coluna):
        #Aqui ele ve quantas rainhas ja existe e 
        
        for linha in range(self.quant):
            if(estadoAtual.estado[linha][coluna] == "Q"):
                estadoAtual.estado[linha][coluna] = '*'
                break
         
        estadoAtual.estado[random.randrange(8)][coluna] = "Q"
        estadoAtual.setCusto(self.testePosicao(estadoAtual.getEstado(),self.quant))
        return estadoAtual

    def testeDeObjetividade(self):
        if(self.getCusto() <=0):
            return True
        else:
            return False

    def sucessora(self,estadoAtual,tipoBusca,tipoProblema,sucessoresMaximo,temperatura,coeficiente):
        #Aqui ele ve quantas rainhas ja existe e 
        valores = []
        for linha in range(self.quant):
            for coluna in range(self.quant):
                if(estadoAtual.estado[coluna][linha] == "Q"):
                    for linhaAux in range(self.quant):
                        aux = deepcopy(estadoAtual.estado)
                        aux[coluna][linha] = '*'
                        if(linhaAux!=coluna):
                            aux[linhaAux][linha] = "Q"
                            valores.append([aux,self.testePosicao(aux)])
                    break
        return tipoBusca.inserir(valores,estadoAtual,tipoProblema,self.quant,sucessoresMaximo,temperatura,coeficiente)
def gerarMatriz(quant):
    matriz = []
    for c in range(quant):
        linha = []
        for l in range(quant):
            linha.append("*")
        matriz.append(linha)
    return matriz

        