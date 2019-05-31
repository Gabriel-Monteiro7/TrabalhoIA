# Depois do destino os três outros atributos são o tipo de busca e
#busca(vetorTotal, Arad.estado, Bucharest.estado, 1, [], None,2)
# se ele tem lista de visitados, so funciona a lista de visitados
# para o metodo de profundidade e por ultimo se ele for profundidade limitada, nunca
# vai poder a junção de dois metodos
from MapaDaRomenia import MapaDaRomenia
from Problema import Problema
mapaRomenia = MapaDaRomenia()
origem = mapaRomenia.Arad.estado
destino = mapaRomenia.Bucharest.estado
#1 == Largura #2 == Profundidade #3 == Custo Uniforme
#ultimo parametro é o tipo de busca se for por profundidade 
#[] = se for lista de visitados 
#int se for limitado
#Object se for interativa
Problema(mapaRomenia.opcao(),origem,destino,2,{"interacoes":3})