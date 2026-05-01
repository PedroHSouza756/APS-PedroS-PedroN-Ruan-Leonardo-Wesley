import os # interage com sistema operacional

class ViewTSP:

    @staticmethod
    def escolher_arquivo():
        arquivos = os.listdir("data")   #lista todos arquivos na pasta data

        print("\nArquivos:\n0 para sair") 
        for i, f in enumerate(arquivos):  # percorre todos os arquivos 
            print(f"{i+1} - {f}")   # mostra todos eles com numero do lado
        while True:
            try:
                op = int(input("Escolha: ")) 

                if op == 0:
                    return None 
                elif 1 <= op <= len(arquivos):
                    return arquivos[op-1] # para evitar o erro, começamos o array no 1 , por isso subtraimos a escolha
                else:
                    print("Opção inválida! Escolha um número da lista.")
            except ValueError:
                print("Digite um número válido.")
  

    @staticmethod
    def escolher_algoritmo():
        print("\n1-Busca em Profundidade 2-Busca em Largura 3-Ramos e Poda 4-Heurística 5-Todos 0-Trocar") # escolha de qual algoritmo for usar
        while True:
            try:
                opcao = int(input("Escolha: "))
                if 0 <= opcao <= 5:
                    return opcao
                else:
                    print("Opção inválida. Escolha entre 0 e 5.")
            except ValueError:
                print("Digite um número válido.")

    @staticmethod
    def mostrar(resultados):  # mostra um menu com as informações - dicionario
        for nome, dados in resultados.items():  # nome do algoritmo +  informaçoes 
            print(f"\n{nome}") # Qual algoritmo 
            print(f"Custo: {dados['custo']:.2f}") # Custo com 2 casas decimais
            print(f"Tempo: {dados['tempo']:.4f} ms") # Tempo com 4 casas decimais
            print(f"Nós visitados: {dados['nos']}") # Qntd de nos visitados 
            print(f"Caminho: {dados['caminho']}") # Caminho que fez nessa solução