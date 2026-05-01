class Heuristic:  # Heuristica Vizinho Prox., ou seja escolhe a cidade mais proxima nao visitada, a primeira que estudamos em aula
    def solve(self, g):
        visitado = [False] * g.size  # Começa com todos false
        caminho = [0] # 0 é o inicial
        visitado[0] = True  # Primeira cidade visitada

        for _ in range(g.size - 1):
            ultimo = caminho[-1] # escolhe a ultima cidade do caminho atual, ou seja a cidade onde estou

            menor_distancia = float("inf")  # valor infinito entao qualquer opção vai ser melhor
            proximo = -1 # qual cidade será escolhida

            for i in range(g.size): # verifica todas as cidades
                if not visitado[i]: # se ela nao foi visitada
                    distancia = g.get_weight(ultimo, i) # faz o calculo da distancia da cidade atual até a cidade i

                    if distancia < menor_distancia: # sempre escolhe a menor cidade disponível
                        menor_distancia = distancia
                        proximo = i

            caminho.append(proximo) # adiciona a cidade escolhida ao caminho
            visitado[proximo] = True # agora essa cidade foi visitada

        caminho.append(0) # adiciona a primeira cidade novamente, ou seja fez o caminho completo

        custo = sum(g.get_weight(caminho[i], caminho[i+1]) for i in range(len(caminho)-1)) # Soma todas as distâncias entre cidades consecutivas
        return caminho, custo, 0 # faz o retorno da rota encontrada, distancia total, e quantidade de nós, mas ela só faz um único caminho