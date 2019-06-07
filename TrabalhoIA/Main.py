from agenteBuscaLocal import AgenteLocal
from rainhas import Rainha
from oitoPeca import Oitopeca
from buscaLargura import BuscaLargura
from buscaProfundidade import BuscaProfundidade
# quantidade = 8
# AgenteLocal(quantidade,BuscaProfundidade,Rainha(8),None,Rainha)
quantidade = 3
AgenteLocal(quantidade,BuscaProfundidade,[],Oitopeca(quantidade,[[2,3,5],[4,6,7],[8,1,""]]),Oitopeca(quantidade,[[1,2,3],[4,5,6],[7,8,""]]),Oitopeca)

