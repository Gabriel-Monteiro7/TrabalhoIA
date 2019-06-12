#Tipo Agente
from BuscaSemInformacao.agente import Agente
from BuscaSemInformacaoMapa.agente import AgenteMapa

#Tipo Problema
from BuscaSemInformacao.rainhas import Rainha
from BuscaSemInformacao.oitoPeca import Oitopeca
from BuscaSemInformacaoMapa.mapaDaRomenia import MapaDaRomenia

#Tipo Busca
from TipoBusca.buscaLargura import BuscaLargura
from TipoBusca.buscaProfundidade import BuscaProfundidade
from TipoBusca.buscaCustoUniforme import BuscaCustoUniforme




#BuscaCustoUniforme
#BuscaLargura
#BuscaProfundidade tem 3 parametro : []  = lista de visitados. int = limitada. {} = interativo
#Se a busca for diferente de Profundidade esse parametro é descatado

# quantidade = 20
# Agente(quantidade,BuscaLargura,None,Rainha(quantidade),None,Rainha)

# quantidade = 3
# Agente(quantidade,BuscaLargura,[] ,None,Oitopeca(quantidade,[[1,2,3],[4,5,6],[7,8,""]]),Oitopeca)

# mapaRomenia = MapaDaRomenia()
# AgenteMapa(BuscaLargura,[],MapaDaRomenia(None,mapaRomenia.Arad.estado),MapaDaRomenia(None,mapaRomenia.Bucharest.estado),MapaDaRomenia)

