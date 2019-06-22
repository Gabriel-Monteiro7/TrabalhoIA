#Agente
from Agente.agente import Agente

#Tipo Problema
from BuscaSemInformacao.rainhas import Rainha
from BuscaSemInformacao.oitoPeca import Oitopeca
from BuscaSemInformacao.mapaDaRomenia import MapaDaRomenia
#com Informação
from BuscaComInformacao.oitoPeca import OitopecaComInformacao

#Tipo Busca
from TipoBusca.buscaLargura import BuscaLargura
from TipoBusca.buscaProfundidade import BuscaProfundidade
from TipoBusca.buscaCustoUniforme import BuscaCustoUniforme
#Serve mais quando se tem informar 
from TipoBusca.buscaA_Estrela import BuscaA_Estrela


#Agente(tamanhoDaMatriz,TipoBusca,TipoDaProfundidade ,EstadoInicial,EstadoFinal,TipoProblema)

#BuscaCustoUniforme
#BuscaLargura
#BuscaProfundidade tem 3 parametro : []  = lista de visitados. int = limitada. {} = iterativo
#Se a busca for diferente de Profundidade esse parametro é descatado

# quantidade = 8
# Agente(quantidade,BuscaProfundidade,{},Rainha(quantidade),None,Rainha)

quantidade = 3
Agente(quantidade,BuscaA_Estrela,{},OitopecaComInformacao(quantidade,[[0,8,3],[1,7,6],[5,2,4]]),OitopecaComInformacao(quantidade,[[1,2,3],[4,5,6],[7,8,0]]),OitopecaComInformacao)

# quantidade = 3
# Agente(quantidade,BuscaLargura,{},Oitopeca(quantidade,[[0,2,3],[1,5,6],[7,8,4]]),Oitopeca(quantidade,[[1,2,3],[4,5,6],[7,8,0]]),Oitopeca)

# mapaRomenia = MapaDaRomenia()
# AgenteMapa(BuscaProfundidade,{},MapaDaRomenia(None,mapaRomenia.Arad.estado),MapaDaRomenia(None,mapaRomenia.Bucharest.estado),MapaDaRomenia)

