from No import No
from copy import deepcopy
import random

class Oitopeca(No):
    def __init__(self,quant,estado = None,pai=None,custo=0):
        self.estado = estado
        self.quant = quant
        super().__init__(self.estado,pai,custo)

    def testeDeObjetividade(self,estadoAtual,estadoFinal,borda):
        if(estadoAtual.getEstado() == estadoFinal.getEstado()):
            return True
        else:
            return False

    def sucessora(self,estadoAtual,borda,tipoBusca,tipoProblema,estadoFinal,listaVisitados,limite):

        for linha in range(self.quant):
            for coluna in range(self.quant):
                if(estadoAtual.estado[linha][coluna] == 0):
                    movimentos = self.movimento(estadoAtual,linha,coluna)
                     #Aqui os movimentos encontrados sao embaralhados
                    random.shuffle(movimentos)
                    #Aqui se cria os filhos que sao add na borda e o tipo da busca que vai definir a posicao de insercao
                    for item in movimentos:
                        borda = tipoBusca.inserir(item,estadoAtual,borda,self.quant,1,tipoProblema,listaVisitados,limite)
                    return borda
       
    def movimento(self,estadoAtual,linha,coluna):
        movimento = []

        if(linha !=self.quant-1):#Movimento cima
            auxEstado = deepcopy(estadoAtual.getEstado())
            auxEstado[linha][coluna] = auxEstado[linha+1][coluna]
            auxEstado[linha+1][coluna] = 0
            movimento.append(auxEstado)
            
        if(linha !=0):#Movimento baixo
            auxEstado = deepcopy(estadoAtual.getEstado())
            auxEstado[linha][coluna] = auxEstado[linha-1][coluna]
            auxEstado[linha-1][coluna] = 0
            movimento.append(auxEstado)

        if(coluna !=self.quant-1):#Movimento esquerda
            auxEstado = deepcopy(estadoAtual.getEstado())
            auxEstado[linha][coluna] = auxEstado[linha][coluna+1]
            auxEstado[linha][coluna+1] = 0
            movimento.append(auxEstado)

        if(coluna !=0):#Movimento direita
            auxEstado = deepcopy(estadoAtual.getEstado())
            auxEstado[linha][coluna] = auxEstado[linha][coluna-1]
            auxEstado[linha][coluna-1] = 0
            movimento.append(auxEstado)
        return movimento
