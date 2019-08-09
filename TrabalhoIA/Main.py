#Agente
from Agente.agente import Agente
from Agente.agenteLocal import AgenteLocal
from Agente.agenteGenetico import AgenteGenetico

#Tipo Problema
from BuscaSemInformacao.rainhas import Rainha
from BuscaSemInformacao.oitoPeca import Oitopeca
from BuscaSemInformacao.mapaDaRomenia import MapaDaRomenia
#com Informação
from BuscaComInformacao.oitoPeca import OitopecaComInformacao
#Local
from BuscaLocal.rainhas import RainhaLocal
#Tipo Busca
from TipoBusca.buscaLargura import BuscaLargura
from TipoBusca.buscaProfundidade import BuscaProfundidade
from TipoBusca.buscaCustoUniforme import BuscaCustoUniforme
#Serve mais quando se tem informar 
from TipoBusca.buscaA_Estrela import BuscaA_Estrela
from TipoBusca.buscaGulosa import BuscaGulosa

from TipoBusca.descidaDaEncosta import DescidaEncosta
from TipoBusca.recozimentoSimulado import RecozimentoSimulado
from TipoBusca.algoritmoGenetico import AlgoritmoGenetico



#Agente(tamanhoDaMatriz,TipoBusca,TipoDaProfundidade ,EstadoInicial,EstadoFinal,TipoProblema)

#BuscaCustoUniforme
#BuscaLargura
#BuscaProfundidade tem 3 parametro : []  = lista de visitados. int = limitada. {} = iterativo
#Se a busca for diferente de Profundidade esse parametro é descatado

# quantidade = 20
# Agente(quantidade,BuscaProfundidade,None,Rainha(quantidade),None,Rainha)

# quantidade = 8
# rainha = RainhaLocal(quantidade)
# rainha.setEstado([['*', '*', '*', '*', '*', '*', '*', '*'],
# ['*', '*', '*', '*', '*', '*', '*', '*'],
# ['*', '*', '*', '*', '*', '*', '*', '*'],
# ['*', '*', '*', 'Q', '*', '*', '*', '*'],
# ['Q', '*', '*', '*', 'Q', '*', '*', '*'],
# ['*', 'Q', '*', '*', '*', 'Q', '*', 'Q'],
# ['*', '*', 'Q', '*', '*', '*', 'Q', '*'],
# ['*', '*', '*', '*', '*', '*', '*', '*']])
# AgenteLocal(quantidade,DescidaEncosta,rainha,RainhaLocal)

# quantidade = 8
# rainha = RainhaLocal(quantidade)
# rainha.setEstado([['*', '*', '*', '*', '*', '*', '*', '*'],
# ['*', '*', '*', '*', '*', '*', '*', '*'],
# ['*', '*', '*', '*', '*', '*', '*', '*'],
# ['*', '*', '*', 'Q', '*', '*', '*', '*'],
# ['Q', '*', '*', '*', 'Q', '*', '*', '*'],
# ['*', 'Q', '*', '*', '*', 'Q', '*', 'Q'],
# ['*', '*', 'Q', '*', '*', '*', 'Q', '*'],
# ['*', '*', '*', '*', '*', '*', '*', '*']])
# AgenteLocal(quantidade,RecozimentoSimulado,rainha,RainhaLocal,8,100,0.9)
for item in range(10):
    print(item)
    quantidade = 8
    rainha = RainhaLocal(quantidade)
    rainha.setEstado([['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', 'Q', '*', '*', '*', '*'],
    ['Q', '*', '*', '*', 'Q', '*', '*', '*'],
    ['*', 'Q', '*', '*', '*', 'Q', '*', 'Q'],
    ['*', '*', 'Q', '*', '*', '*', 'Q', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*']])
    AgenteGenetico(quantidade,AlgoritmoGenetico,rainha,RainhaLocal,30)

# quantidade = 3
# Agente(quantidade,BuscaA_Estrela,{},OitopecaComInformacao(quantidade,[[8,6,2],[1,7,0],[5,3,4]]),OitopecaComInformacao(quantidade,[[1,2,3],[4,5,6],[7,8,0]]),OitopecaComInformacao)

# quantidade = 3
# Agente(quantidade,BuscaCustoUniforme,{},Oitopeca(quantidade,[[3,1,2],[4,8,7],[0,6,5]]),Oitopeca(quantidade,[[0,1,2],[3,4,5],[6,7,8]]),Oitopeca)

# mapaRomenia = MapaDaRomenia()
# Agente(0,BuscaCustoUniforme,{},MapaDaRomenia(None,mapaRomenia.Arad.estado),MapaDaRomenia(None,mapaRomenia.Bucharest.estado),MapaDaRomenia)
