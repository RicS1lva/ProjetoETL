# ProjetoETL

### - Fiz esta planilha com alguns produtos que são vendidos em um mercado fictício Onde os produtos categorizados como "Secos", entrariam em promoção.
![image](https://github.com/RicS1lva/ProjetoETL/assets/143663432/897bcfb7-ebdd-433a-872f-23863df17d23)

### - Para calcular o valor após o desconto, montei a fórmula com .loc, para alterar somente a categoria desejada.
```python
url_cod = 'ProjetoETL/Tabelas_de_precificacao/Precificacao_antes _do_desconto.csv'`

df_product = pd.read_csv(url_cod, sep=';')
print(df_product)

df_product.loc[df_product.Categoria == "Secos", 'Valor_Kg'] -= df_product.loc[df_product.Categoria == "Secos", 'Valor_Kg'] *0.25
print(df_product)
```

### - Por fim, transformei o df novamente em CSV, direcionando-o para uma planilha, atualizando sempre com base nos valores padrão.
![image](https://github.com/RicS1lva/ProjetoETL/assets/143663432/6a44a463-9d04-412c-a3f9-ba36903feec9)
