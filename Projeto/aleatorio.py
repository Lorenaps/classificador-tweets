import csv
import random

entrada = "../AnaliseTweets/nomeArquivo_in.csv"
saida = "../AnaliseTweets/nomeArquivo_out.csv"
size = 500
lista_tweets = []

# Esse trecho abre o arquivo de entrada
with open(entrada, 'r', encoding='utf-8') as fin:
    reader = csv.reader(fin, dialect=csv.excel_tab)
    for row in reader:
        # Pega as primeiras 3 colunas: número
        # identificador, data de criação e texto
        # de cada linha
        t = [row[0], row[1], row[2]]
        # Adiciona cada nova linha a lista de tweets
        lista_tweets.append(t)

# Abre arquivo de saída
with open(saida, 'a', encoding='utf-8') as fout:
    # Gera nova lista randomizada
    nova_lista = random.sample(lista_tweets, size)
    writer = csv.writer(fout, dialect=csv.excel_tab)
    # Salva no arquivo aberto anteriormente
    writer.writerows(nova_lista)

