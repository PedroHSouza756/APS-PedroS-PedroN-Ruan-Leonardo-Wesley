import time # usa para contar tempo de execução
from model.BuscaEmProfundidade import BeP
from model.BuscaEmLargura import BeL
from model.RamosEPoda import BranchBound
from model.Heuristica import Heuristic

class ControladorTSP:
    def __init__(self, grafo):  # recebe o grafo
        self.grafo = grafo

    def executar(self, algoritmo): # recebe o algoritmo e executa ele com o grafo
        inicio = time.perf_counter() # marca o tempo antes de começar o algoritmo
        caminho, custo, nos = algoritmo.solve(self.grafo) # usa o solve do algoritmo
        tempo = (time.perf_counter() - inicio) * 1000 # calcula o tempo que demorou em mili segundos

        return {
            "caminho": caminho,
            "custo": custo,
            "tempo": tempo,
            "nos": nos
        } # retorna as informações da execução

    def executar_selecionado(self, opcao): # escolhe qual algoritmo rodar
        algoritmos = {
            "Busca em Profundidade": BeP(),
            "Busca em Largura": BeL(),
            "Ramos e Poda": BranchBound(),
            "Heurística": Heuristic()
        } # menu de escolha


        resultados = {} # armazena o resultado

        if opcao == 5: # se escolher 5 roda todos os algoritmos
            for nome, algoritmo in algoritmos.items(): # percorre o dicionario de algoritmos 
                resultados[nome] = self.executar(algoritmo) # e roda todos eles e armazena os resultados de cada algoritmo 
        else:
            chave = list(algoritmos.keys())[opcao - 1] # escolhe a opção do usuário menos 1, porque começa no 0
            resultados[chave] = self.executar(algoritmos[chave])  # executa só o algoritmo escolhido

        return resultados