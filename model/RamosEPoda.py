class BranchBound:
    def solve(self, g):
        self.melhor = float('inf') # Começa com o melhor, ou seja menor custo, e inicia com infinito para qualquer solução ser aceita
        self.caminho = [] # guarda o melhor caminho
        self.nos = 0 # conta quantos nos foram explorados

        visitado = [False] * g.size # todos nao foram visitados
        visitado[0] = True # a inicia com a primeira cidade

        self._bb(g, 0, visitado, [0], 0) # chama a função e envia os valores cidade atual, caminho inicial e o custo
        return self.caminho, self.melhor, self.nos # retorna o melhor caminho, custo do caminho, e estados explorados

    def _bb(self, g, atual, visitado, caminho, custo):
        self.nos += 1 # cada vez que passar adiciona que mais um no foi explorado

        if len(caminho) == g.size: # se ja visitou todas as cidades
            total = custo + g.get_weight(atual, 0) # Fecha o ciclo voltando para cidade 0
            if total < self.melhor: # se o caminho é melhor que o que esta armazenado atualmente
                self.melhor = total # melhor custo
                self.caminho = caminho + [0] # melhor rota
            return # termina aqui

        for i in range(g.size): # caso ainda nao visitou
            if not visitado[i]:
                novo_custo = custo + g.get_weight(atual, i) # custo ate a nova cidade

                # Branch and Bound, aqui que vem a poda
                if novo_custo >= self.melhor: # se o valor atual for pior que o melhor ja corta o caminho por aqui
                    continue

                visitado[i] = True # marca a cidade como visitada
                self._bb(g, i, visitado, caminho + [i], novo_custo) # roda a propria def com os valores atuais
                visitado[i] = False # desfaz esse caminho, evita travar o algoritmo em um valor fixo


                # Entra no caminho -> marca como visitado -> quando terminou o caminho volta tudo
                # O caminho precisa estar livre para outro teste, é um brute force porem cortando caminhos que são custosos , ou seja mais rapido
                