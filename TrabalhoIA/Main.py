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

# quantidade = 8
# Agente(quantidade,BuscaCustoUniforme,{},Rainha(8),None,Rainha)

quantidade = 3
Agente(quantidade,BuscaLargura,{},Oitopeca(quantidade,[[7,2,4],[5,"",6],[8,3,1]]),Oitopeca(quantidade,[["",1,2],[3,4,5],[6,7,8]]),Oitopeca)

# mapaRomenia = MapaDaRomenia()
# AgenteMapa(BuscaProfundidade,[],MapaDaRomenia(None,mapaRomenia.Arad.estado),MapaDaRomenia(None,mapaRomenia.Bucharest.estado),MapaDaRomenia)

