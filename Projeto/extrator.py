from twitter import *
import re


class Extrator:


    def __init__(self):
        # Chave utilizada para que a aplicação se identifique perante o Twitter.
        CONSUMER_KEY= ''
        # Chave para a aplicação provar sua autenticidade
        CONSUMER_SECRET = ''
        #Após a identificação é preciso que a aplicação envie esse código para
        #  que o serviço possa identificar qual o nível de acesso que ela possui;
        OAUTH_TOKEN = ''
        #Chave para a aplicação provar sua autenticidade com relação ao Access Token
        OAUTH_TOKEN_SECRET = ''
        self.api = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
        self.lista_tweets = []


    def busca(self, termo, idioma, quantidade):
        tweets = self.api.search.tweets(q=termo, lang=idioma, count=quantidade)
        for resultado in tweets["statuses"]:
            # Expressão regular para identificar tweets marcados como retweets
            retweet = re.search('RT ', resultado["text"])
            # Se o tweete em questão não for um retweet ele é adicionado a
            # lista de tweets a ser utilizada
            if retweet == None:
                self.lista_tweets.append((resultado["id_str"],
                                          resultado["created_at"],
                                          resultado["text"],
                                          resultado["user"]["location"]))

