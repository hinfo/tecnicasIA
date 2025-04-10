import copy
import os

from ag import AG


if __name__ == "__main__":
    os.system('clear') #Linux

    tamanho_populacao = int(input("Tamanho da população: "))
    estado_final = input("Palavra desejada: ")
    taxa_selecao = int(input("Taxa de seleção (entre 20 a 40%): "))
    taxa_selecao = 30
    taxa_reproducao = 100 - taxa_selecao
    taxa_mutacao = int(input("Taxa de mutação (entre 5 a 10%): "))
    qtd_geracoes = int(input("Quantidade de gerações: "))
    qtd_geracoes = 50

    rotas = []
    nova_populacao = []
    
    AG.gerar_populacao(rotas, tamanho_populacao, estado_final)
    rotas.sort()
    print("Geracao 1")
    AG.exibir(rotas)

    for i in range(1, qtd_geracoes):
        AG.selecionar_por_torneio(rotas, nova_populacao, taxa_selecao)
        
        AG.reproduzir(rotas, nova_populacao, taxa_reproducao, estado_final)
        
        if (i % (len(rotas) / taxa_mutacao) == 0):
            AG.mutar(nova_populacao, estado_final)
        
        rotas.clear()
        rotas = copy.deepcopy(nova_populacao)
        nova_populacao.clear()
        rotas.sort()

        print(f"\n\nGeração: {(i + 1)}")
        AG.exibir(rotas)
        