from agenteBuscaLocal import AgenteLocal
from rainhas import Rainha
from buscaLargura import BuscaLargura
from oitoPeca import Oitopeca
# quantidade = 8
# AgenteLocal(quantidade,BuscaLargura,Rainha(8))
quantidade = 3
AgenteLocal(quantidade,BuscaLargura,Oitopeca(quantidade,[[2,3,5],[4,6,7],[8,1,""]]),Oitopeca(quantidade,[[5,6,2],[1,8,4],[7,3,""]]),Oitopeca)

