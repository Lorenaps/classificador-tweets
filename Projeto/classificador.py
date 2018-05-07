# coding=utf-8
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation
from sklearn.metrics import precision_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from preprocessador import PreProcessador
import csv

arquivo_in_cn = "./contraNegros/contraNegros_08_out_sem_id.csv"
arquivo_in_cm = "./contraMulheres/contraMulheres_08_out_sem_id.csv"

arquivo_out_cn = "../AnaliseTweets/contraNegros/contraNegros_clf.csv"
arquivo_out_cm = "../AnaliseTweets/contraMulheres/contraMulheres_clf.csv"

# Instância do pré-processador
p = PreProcessador()

# Carregar os dados do arquivo e faz o pré-processamento para o arquivo
#  de dados referente a DO direcionado aos negros
p.normalizar_dados(arquivo_in_cm)
# Função que separa os tweets e os rótulos
p.get_tweets_e_rotulos()

# Carregar os dados do arquivo e faz o pré-processamento para o arquivo
#  de dados referente a DO direcionado às mulheres
#p.normalizar_dados(arquivo_in_cn)
#p.get_tweets_e_rotulos()
#p.print_lista(p.rotulos_tweets)

# Divide o conjunto de dados para treinamento e teste do classificador,
# de acordo com o parâmetro test_size (que nesse caso está indicando
# uma divisão de 30% para o conjunto de teste e 70% para o treinamento)
X_treino, X_teste, Y_treino, Y_teste = cross_validation.train_test_split(
     p.tweets, p.rotulos_tweets, test_size=0.3, random_state=0)

print("Treino: ", len(X_treino), " - ", len(Y_treino))
print("Teste: ", len(X_teste), " - ", len(Y_teste))

# Criando o extrator de features, stop words está marcado para
# None porque as stopwords já foram retiradas no pré-processamento.

#Extrator de features para unigrama
vectorizer = CountVectorizer(min_df=1, stop_words=None)

# Treinamento do extrator de features com o conjunto de treinamento
X_treino_vec = vectorizer.fit_transform(X_treino)
print("Quantidade de features extraídas: ",len(vectorizer.get_feature_names()))

print(vectorizer.get_feature_names())

# Criação do classificador
clf = GaussianNB()

# Treinamento do Classificador
clf.fit(X_treino_vec.toarray(), Y_treino)

# Extraíndo features do conjunto de teste
X_teste_vec = vectorizer.transform(X_teste)

# Executando o classificador com o conjunto de teste
pred = clf.predict(X_teste_vec.toarray())

# Rótulos usados para ordenar os resultados nas funções que retornam
#  os valores para avaliação do classificador
classes=["0", "1"]

# Avaliando a matriz de confusão
print("Matriz de confusão:")
print(confusion_matrix(Y_teste, pred, labels=classes))

# Avaliando a acurácia
print("Accuracy score:")
print(accuracy_score(Y_teste, pred))

# Avaliando a precisão
print("Precision score:")
print(precision_score(Y_teste, pred, average=None, labels=classes))

# Avaliando o recall
print("Recall score:")
print(recall_score(Y_teste, pred, average=None, labels=classes))

# Avaliando o f-score
print("F-score score:")
print(f1_score(Y_teste, pred, average=None, labels=classes))


# Formatar e salvar um arquivo para exibir o texto, o seu rótulo correto
# e a predição feita pelo classificador
# cmp = []
# for a,b,c in zip(X_teste, Y_teste, pred):
#     nlista = [a,b,c]
#     cmp.append(nlista)
#
# with open(arquivo_out_cn, 'a', encoding='utf-8') as fout:
#     writer = csv.writer(fout, dialect=csv.excel_tab)
#     writer.writerows(cmp)