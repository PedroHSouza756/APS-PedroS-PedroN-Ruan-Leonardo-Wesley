class BeP:
    def solve(self, g):
        n = g.size  # Guarda o número de nós do grafo
        self.melhor = float('inf') # Melhor custo encontrado, inicia com "inf" porque qualquer solução vai ser menor que o infinito
        self.caminho = [] # Guarda o melhor caminho encontrado.
        self.nos = 0 # Contador de nós explorados.

        # Fizemos o visitado diferente porque, no modelo DFS fizemos uma busca completa até o fim, exploramos um único caminho por vez, diferente do Busca Em Largura que faz vários de uma só vez
        # Dessa forma nao achei que era necessario copiar tudo, e sim editar

        visitado = [False] * n   #inicia com todos estados false
        visitado[0] = True #o primeiro é true porque rodamos o programa 

        self.dfs(g, 0, visitado, [0], 0)
        return self.caminho, self.melhor, self.nos

    def dfs(self, g, atual, visitado, caminho, custo):  # puxa a função dfs
        self.nos += 1 # cada estadoi explorado soma um

        if len(caminho) == g.size: # Se já visitou todas as cidades
            total = custo + g.get_weight(atual, 0) # soma o custo de voltar para a cidade zero
            if total < self.melhor: # se esse caminho for melhor que o anterior
                self.melhor = total # atualiza o melhor custo
                self.caminho = caminho + [0] # caminho completo voltando pro inicio
            return # não continua expandindo caso finalizado

        for i in range(g.size): # tenta todas cidades possiveis
            if not visitado[i]: # so continua se a cidade ainda não foi visitada
                visitado[i] = True # Marca cidade como visitada
                self.dfs(g, i, visitado, caminho + [i], custo + g.get_weight(atual, i)) # vai pra cidade i, adiciona no caminho, soma o custo e continua a busca
                visitado[i] = False # Desfaz a escolha pra testar outro caminho