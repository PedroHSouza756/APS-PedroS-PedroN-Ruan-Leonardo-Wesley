from model.Coordenadas import Coord
import math

class Graph:
    def __init__(self):
        self.size = 0   # é total de nós
        self.weights = []   # matriz de distancia   
        self.coords = {}    # dicionario com coordenadas x y

    def load_from_tsp(self, path):  # le o arquivo e vai montar o grafo
        coords = []  # guarda as coordenadas da cidade se for por coordenadas
        values = []  # guarda os valores da matriz, caso for o formato padrão do grafo

        reading_coords = False  # estamos usando coordenadas
        reading_matrix = False  # ou estamos usando matriz 
        dimension = 0   # numero de cidades
        edge_format = None  # formato da matriz

        with open(path) as f:       # abre o arquivo e executa a leitura linha por linha
            for line in f:      # para cada linha
                line = line.strip() # remove os espaços extras da linha

                if "DIMENSION" in line:                 # armazena a quantidade de cidades que existem no problema
                    dimension = int(line.split(":")[-1].strip())

                if "EDGE_WEIGHT_FORMAT" in line:        # Define como a matriz de distancia está armazenada no arquivo
                    edge_format = line.split(":")[1].strip()

                if "NODE_COORD_SECTION" in line:        # se for por Node Coord, o uso de coordenadas é mudado para True
                    reading_coords = True
                    continue

                if "EDGE_WEIGHT_SECTION" in line:       # se for por Edge Weight utiliza a matriz de distancia
                    reading_matrix = True
                    continue

                if "EOF" in line:                      # para a leitura no fim do arquivo
                    break

                if reading_coords:  # se reading_coords for true
                    parts = line.split()  # separa parts
                    if len(parts) >= 3:  # se tiver 3 separações ou mais
                        coords.append((float(parts[-2]), float(parts[-1])))  # pega a coordenada x e y, ou seja o penultimo e ultimo valor

                elif reading_matrix:
                    values.extend(map(float, line.split()))  # quebra a linha em string, converte todos os elementos em float e adiciona na lista values 

        if coords:
            self._from_coords(coords) # pega os pontos x e y e calcula a distancia entre todas as cidades
        else:
            self._from_matrix(values, dimension, edge_format) # usa diretamente a matriz de distancia fornecidas

    def _from_coords(self, coords):  # utiliza as coordenadas para montar o grafo
        self.size = len(coords) # define quantas cidades existem
        self.weights = [[0]*self.size for _ in range(self.size)] # cria uma matriz de distancias, mas inicia com NxN com 0 em tudo

        for i, (x, y) in enumerate(coords):     # sendo i o indice da cidade 0 1 2 ... e as coordenadas
            self.coords[i] = Coord(x, y)        # coords = [(10,20),(15,25)] vai virar coords[0] = coords[0] = Coord(10,20), coords[1] = Coord(15,25), .......

        for i in range(self.size): # para cada cidade i 
            for j in range(self.size):  # compara com j
                self.weights[i][j] = Coord.dist(self.coords[i], self.coords[j]) # pega cidade i, j, calcula a distancia entre elas e salva no lugar especifico da matriz

    def _from_matrix(self, values, n, fmt): # organiza a lista de valores que fizemos anteriormente "reading_matrix"
        self.size = n   # quantas cidades existem
        self.weights = [[0]*n for _ in range(n)]  # igual a anterior, cria uma matriz NxN com todos os valores sendo 0

        # Usa os modelos mais comuns, Upper_Row e Lower_Diag_Row

        if fmt == "UPPER_ROW":  # verifica se o modelo é Upper_Row
            k = 0       # é o indice da lista "values"
            for i in range(n):                          # percorre apenas a parte de cima da matriz, sem a diagonal, que seria a distancia entre a cidade para ela mesma, 0
                for j in range(i+1, n):                 #   
                    self.weights[i][j] = values[k]      # coloca o valor do "peso" para [i][j]
                    self.weights[j][i] = values[k]      # coloca o valor do "peso" para [j][i]      deixa a matriz simétrica
                    k += 1                              # avança a lista de valores


        elif fmt == "LOWER_DIAG_ROW":   # verifica se o modelo é Lower_Diag_Row
            k = 0      # é o indice da lista "values"
            for i in range(n):                         # percorre apenas a parte de baixo da matriz, mas como o nome do modelo, lower_diag_row, a diagonal principal seria a distancia entre a cidade para ela mesma, 0
                for j in range(i+1):                   #
                    self.weights[i][j] = values[k]     # coloca o valor do "peso" para [i][j]
                    self.weights[j][i] = values[k]     # coloca o valor do "peso" para [j][i]      deixa a matriz simétrica
                    k += 1                             # avança a lista de valores

        else:
            raise Exception("Formato não suportado")

    def get_weight(self, u, v): # consulta a matriz de distancia entre duas cidades
        return self.weights[u][v]