import pandas as pd
import requests
import json

url_cod = 'ProjetoETL/Tabelas_de_precificacao/Precificacao_antes _do_desconto.csv'

df_product = pd.read_csv(url_cod, sep=';')
print(df_product)

df_product.loc[df_product.Categoria == "Secos", 'Valor_Kg'] -= df_product.loc[df_product.Categoria == "Secos", 'Valor_Kg'] *0.25
print(df_product)


df_product.to_csv('C:\Repositórios Git\ProjetoETL\Tabelas_de_precificacao\Precificacao_depois_do_desconto.csv', sep = ';', index=False)


