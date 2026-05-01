from model.Grafo import Graph
from controller.tsp_controller import ControladorTSP
from view.tsp_view import ViewTSP

def principal():
    while True: # Loop que permite a escolha dos arquivos
        arquivo = ViewTSP.escolher_arquivo() # escolhe o arquivo
        if arquivo is None: # fecha programa se for None
            break

        grafo = Graph() # cria um objeto grafo
        grafo.load_from_tsp("data/" + arquivo) # carrega o grafo com as informações armazenadas  
 
        controlador = ControladorTSP(grafo) # cria o controlador responsavel para executar no grafo

        while True:
            opcao = ViewTSP.escolher_algoritmo() # a opção vai ser a escolha do algoritmo

            if opcao == 0: # se for 0 troca o arquivo
                break

            resultados = controlador.executar_selecionado(opcao) # executa a opção que o usuario pediu
            ViewTSP.mostrar(resultados) # mostra os resultados 

if __name__ == "__main__":
    principal()  # inicia o programa