#Importando bibliotecas que serão necessárias

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#A biblioteca seaborn vai buscar um dataset chamado "iris" e carregá-la como um dataframe (csv) em uma variável, que por acaso tem o mesmo nome.
iris = sns.load_dataset("iris")

#mostra as primeiras 5 linhas do dataframe.
print(iris.head())

#traz alguns dados estatísticos do dataframe.
print(iris.describe())

#count provavelmente vai aparecer com 150, isso pode significar:
#todas as linhas estão preenchinas.
#existe uma quantidade igual de linhas com valores missing (vazias)

#verifica quantidade de registros e colunas
print(iris.shape)

#verifica se há valores vazio
print(iris.isna().any())

#informações técnicas, também fornece se há valores nulos.
print(iris.info())