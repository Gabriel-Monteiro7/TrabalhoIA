import time
from No import No


class Problema:
    def __init__(self, problemaSelecionado, origem, destino, tipoBusca=1, buscaProfundidade=None):
        self.problemaSelecionado = problemaSelecionado
        self.origem = origem
        self.destino = destino
        self.tipoBusca = tipoBusca
        self.buscaProfundidade = buscaProfundidade

        busca(self.problemaSelecionado, self.origem,
              self.destino, self.tipoBusca, self.buscaProfundidade)


def exibirResultado(caminho):
    
    if(caminho != False):
        print("Caminho é:", end='')
        for item in caminho:
            print(" -->", item, end='')
        
        


def expande(valor):
    vetor = []
    for item in valor.filho:
        vetor.insert(0, item)
    return vetor


def sucessoraLargura(valor, problemaselecionado, borda):
    aux = expande(problemaselecionado[valor.estado])
    for item in aux:
        borda.append(No(item.estado, valor))
    return borda


def sucessoraProfundidade(valor, problemaselecionado, borda, buscaProfundidade):
    aux = expande(problemaselecionado[valor.estado])
    for item in aux:
        if(buscaProfundidade is []):
            if(not (item.estado in buscaProfundidade)):
                borda.insert(0, No(item.estado, valor))
        elif (buscaProfundidade is int):
            if(buscaProfundidade > valor.getProfundidade()):
                borda.insert(0, No(item.estado, valor))
            else:
                return False
        else:
            borda.insert(0, No(item.estado, valor))
    return borda


def testeObjetivo(valor, destino):
    if(valor == destino):
        return True


def busca(problemaselecionado, origem, destino, tipo, buscaProfundidade):
    print()
    if(tipo == 1):
        tipo = "Largura"
    elif(tipo == 2):
        tipo = "Profundidade"
    else:
        tipo = "Custo Uniforme"

    interacoes = 1
    if(buscaProfundidade is int and tipo == "Profundidade"):
        tipo = tipo + " limitada"

    elif(buscaProfundidade is [] and tipo == "Profundidade"):
        buscaProfundidade.append(valor.estado)
        tipo = tipo + " com lista de visitados"

    elif(type(buscaProfundidade) is dict and tipo == "Profundidade"):
        tipo = tipo + " interativa"
        interacoes = buscaProfundidade['interacoes']
    print("Busca por", tipo)
    print("")
    print("Origem:", origem, "Destino:", destino)
    print("")

    aux = 0
    while(interacoes >= aux):
        
        
        borda = []
        valor = problemaselecionado[origem]
        borda.append(valor)
        inicio = time.time()
        count = 1
        if(interacoes>1):
            print("Interação:",aux)
        while(True):
            borda.pop(0)
            print("Valor atual: " + valor.getEstado())
            if((borda == [] and count > 1) or count > 1000):
                print("Valor não existe")
                return False
            if(testeObjetivo(valor.getEstado(), destino) or valor.getProfundidade()==aux):
                break
            else:
                if(tipo == "Largura"):
                    borda = sucessoraLargura(valor, problemaselecionado, borda)
                else:
                    borda = sucessoraProfundidade(
                        valor, problemaselecionado, borda, buscaProfundidade)
                    if(borda == False):
                        print("")
                        print("Limite foi alcançado, busca vai parar")
                        break
                valor = borda[0]
                if(buscaProfundidade is []):
                    buscaProfundidade.append(borda[0].estado)
                count += 1

        print("-------------------------")
        fim = time.time()
        tempoTotal = (fim - inicio)*1000
        print("Tempo total: %0.1f" % tempoTotal, "ms")
        print("Quantidade de passos:", count)
        print("Profundidade:", valor.getProfundidade())

        caminho = []
        while(valor != None):
            caminho.insert(0, valor.estado)
            valor = valor.pai
        exibirResultado(caminho)
        print("\n")
        aux += 1
        
