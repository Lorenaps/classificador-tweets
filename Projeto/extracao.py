from time import sleep
from datetime import datetime
from extrator import Extrator
from stringBusca import StringBusca
import csv

rodada_atual = 0
rodada_total = 5
quantidade = 100
idioma = "pt"

strings = StringBusca()

# Laço de repetição responsável por garantir a execução das rodadas com intervalo
#  de duas horas
while rodada_atual <= rodada_total:
    print("Extração de tweets contra negros " + datetime.now().isoformat('T'))
    print("Rodada de coletas: " + str(rodada_atual) + " de " + str(rodada_total))

    # Laço de repetição para executar a busca para cada string dentro da lista
    #  de strings contra negros
    for n_grama in strings.n_gramas_contra_negros:
        # Abre arquivo CSV para salvar os resultados da busca para a string atual
        with open('./Contra_Negros/' + str(datetime.now().day) + "_" +
              str(datetime.now().month) + "_" + str(datetime.now().year) +
              "_" + n_grama + '.csv', 'a', encoding='utf-8') as f:
            # Instancia a Classe Extrator
            twitter = Extrator()
            #Chama a função de Busca
            twitter.busca(n_grama, idioma, quantidade)
            # Instancia objeto que formata os dados passados por
            # parâmetro, para dados separados por valores
            writer = csv.writer(f, dialect=csv.excel_tab)
            # Escreve no arquivo criado anteriormente
            writer.writerows(twitter.lista_tweets)

    print("Extração de tweets contra mulheres " + datetime.now().isoformat('T'))

    # Laço de repetição para executar a busca para cada string dentro da lista
    #  de strings contra mulheres
    for n_grama in strings.n_gramas_contra_mulheres:
        # Abre arquivo CSV para salvar os resultados da busca para a string atual
        with open('./Contra_Mulheres/' + str(datetime.now().day) + "_" +
              str(datetime.now().month) + "_" + str(datetime.now().year) +
              "_" + n_grama + '.csv', 'a', encoding='utf-8') as g:
            # Instancia a Classe Extrator
            twitter = Extrator()
            # Chama a função de Busca passando a string de busca,
            # o idioma e a quantidade
            twitter.busca(n_grama, idioma, quantidade)
            # Instancia objeto que formata dados para dados separados por valores
            writer = csv.writer(g, dialect=csv.excel_tab)
            # Escreve no arquivo criado anteriormente
            writer.writerows(twitter.lista_tweets)

    print("Esperando próxima rodada - " + datetime.now().isoformat('T'))
    rodada_atual = rodada_atual + 1
    # Faz o código "dormir" por duas horas
    sleep(7200)
