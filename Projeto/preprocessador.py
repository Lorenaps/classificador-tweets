# coding=utf-8
import csv
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import re


class PreProcessador:


    def __init__(self):
        # Todas as informações vindas do csv
        self.dados = []
        # Apenas os tweets pré processados
        self.tweets = []
        # Rótulos do tweet
        self.rotulos_tweets = []


    # Função para carregar os dados de um arquivo csv e fazer o
    # pré-processamento dos mesmos
    def normalizar_dados(self, arquivo):
        contador = 0
        # Abre o arquivo csv indicando o encoding como utf-8
        with open(arquivo, 'r', encoding='utf-8') as f:
            # Indica que o arquivo está separado por TAB
            reader = csv.reader(f, dialect=csv.excel_tab)
            for row in reader:
                # Aplica os filtros para retirada de menções, links,
                # emojis, pontuação, stopwords e espaços em branco
                # nas extremidades
                row[2] = self.retirar_stopwords(self.retirar_pontuacao(
                    self.retirar_emoji(self.retirar_link(self.retirar_mention(
                    row[2])))).lower()).strip()
                # Separa a frase em tokens (palavras) indicando o idioma
                row[2] = nltk.word_tokenize(row[2], 'portuguese')
                # Realiza o processo de stemming
                row[2] = self.stemming(row[2])
                self.dados.append(row)
                contador = contador + 1

        print("TOTAL TWEETS:" + str(contador))

    # Essa função normaliza os dados mas não aplica o stemming
    def normalizar_dados_nuvem_palavras(self, arquivo):
        contador = 0
        # Abre o arquivo csv indicando o encoding como utf-8
        with open(arquivo, 'r', encoding='utf-8') as f:
            # Indica que o arquivo está separado por TAB
            reader = csv.reader(f, dialect=csv.excel_tab)
            for row in reader:
                # Aplica os filtros para retirada de menções, links,
                # emojis, pontuação, stopwords e espaços em branco
                # nas extremidades
                row[2] = self.retirar_stopwords(self.retirar_pontuacao(
                    self.retirar_emoji(self.retirar_link(self.retirar_mention(
                        row[2])))).lower()).strip()
                # Separa a frase em tokens (palavras) indicando o idioma
                row[2] = nltk.word_tokenize(row[2], 'portuguese')
                self.dados.append(row)
                contador = contador + 1

        print("TOTAL TWEETS:" + str(contador))

    # Organização dos dados
    def get_tweets_e_rotulos(self):
        self.tweets = self.get_tweets()
        self.rotulos_tweets = self.get_rotulos()

    # Separa os tweets do restante dos dados presente no arquivo e que
    # foram carregados na função normalizar_dados. Na função normalizar_dados
    # para a aplicação da função de stemming primeiro é preciso separar o texto
    # do tweet em tokens(palavras), porém para a função que vai fazer a extração
    # de features, para o classificador, posteriormente, é preciso que os tokens
    # antes separados estejam juntos novamente, por isso essa função (get_tweets)
    # foi feita dessa forma.
    def get_tweets(self):
        nova_lista = []
        espaco = " "
        t = ""
        for palavras in self.dados:
            nova_lista.append(t)
            t = ""
            for palavra in palavras[2]:
                t = t + palavra + espaco #concatena as palavras de cada tweets acrescentando um espaço
        nova_lista.append(t)
        nova_lista.remove('')

        return nova_lista


    # Separa os rótulos(classes) atribuído a cada tweet na classificação
    # manual do restante dos dados presente no arquivo e que foram carregados
    # na função normalizar_dados.
    def get_rotulos(self):
        rotulos_tweets = []
        for row in self.dados:
            rotulos_tweets.append(row[3])
        return rotulos_tweets


    # Filtro para retirar emojis
    def retirar_emoji(self, expr):
        regex_emoji = re.compile(u'['
                                 u'\U0001F300-\U0001F64F'
                                 u'\U0001F680-\U0001F6FF'
                                 u'\u2600-\u26FF\u2700-\u27BF]+',
                                 re.UNICODE)
        return re.sub(regex_emoji, "", expr)

    # Filtro para retirar menções
    def retirar_mention(self, expr):
        regex_mention = re.compile("@([\w])*")
        return re.sub(regex_mention, "", expr)

    # Filtro para retirar link
    def retirar_link(self, expr):
        regex_link = re.compile("http.[\W]*([\w]*.[\w]*[\W][\w]*)")
        return re.sub(regex_link, "", expr)

    # Filtro para retirar pontuação
    def retirar_pontuacao(self, expr):
        regex_pontuacao = re.compile("[^\w ]+")
        return re.sub(regex_pontuacao, " ", expr)

    # Filtro para retirar stopwords
    def retirar_stopwords(self, expr):
        stopwords = nltk.corpus.stopwords.words('portuguese')
        for palavra in stopwords:
            expr = re.sub("\\b(" + palavra + ")\\b", '', expr)
        return (expr)

    # Aplica a função de stemming
    def stemming(self, lista_palavras):
        stemmer = nltk.stem.RSLPStemmer() #stemming para o idioma português do Brasil
        palavras = [stemmer.stem(p) for p in lista_palavras]
        return palavras

    # Imprime os itens de uma lista
    def print_lista(self, lista):
        for item in lista:
            print(item)

