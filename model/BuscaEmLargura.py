from collections import deque # uma fila mais eficiente

class BeL: # Utilizamos FIFO first in, first out, primeiro que entra é o primeiro que sai, é o basico do Busca em Largura
    def solve(self, g):
        fila = deque()
        fila.append(([0], 0, [True] + [False] * (g.size - 1))) # cria uma lista de visitados com tamanho igual ao número de nós,  o nó 0 começa como True (já visitado) e os demais como False

        melhor = float('inf') # é um valor infinito, entao qualquer solução será melhor que a escolha atual
        melhor_caminho = [] # guarda o melhor caminho
        nos = 0  # quantidade de estados explorados (nós da árvore de busca)

        while fila: # Continua enquanto houver estados na fila.

            caminho, custo, visitado = fila.popleft() # remove o primeiro elemento da fila e recupera rota|custo|visitado(quais cidades ja passou)
            nos += 1 # somamos a qntd de nos explorados

            if len(caminho) == g.size:  # se todos nós foram visitados

                total = custo + g.get_weight(caminho[-1], 0)  # Fecha o loop e soma o custo do último nó até o nó 0.
                if total < melhor: # verifica se é melhor que o atual, sempre que rodar a primera vez será melhor, por conta do "inf"
                    melhor = total # atualiza melhor custo
                    melhor_caminho = caminho + [0] # guarda o caminho 0 > x > y > 0
                continue # vai pro prox estado da fila

            for i in range(g.size): # percorre todos os nós
                if not visitado[i]: #considera os que nao foram visitados
                    v = visitado[:] #faz uma copia da lista de visitados, fazemos isso para nao modificar o original, ou seja teremos um "historico" dos grafos
                    v[i] = True # marca o nó como visitado
                    fila.append((caminho + [i], custo + g.get_weight(caminho[-1], i), v)) # adiciona um novo estado na fila, novo caminho | custo | e a lista atualizada de visitados

        return melhor_caminho, melhor, nos   # ao final de tudo retorna o melhor caminho encontrado ,custo mínimo,número de nós explorados