from .preprocessador import PreProcessador

# Caminho e nome dos arquivos
arquivo_in_cn = "../AnaliseTweets/contraNegros/contraNegros_08_in.csv"
arquivo_in_cm = "../AnaliseTweets/contraMulheres/contraMulheres_08_in.csv"

# Instância do pré-processador
p = PreProcessador()

# Carregar os dados do arquivo e faz o pré-processamento para o arquivo
#  de dados referente a DO que se deseja analisar
p.normalizar_dados_nuvem_palavras(arquivo_in_cn)
p.get_tweets_e_rotulos()
p.print_lista(p.tweets)

