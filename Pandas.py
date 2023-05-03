import pandas as pd

# cria um dataframe com informações de vendas
vendas = {'Produto': ['P1', 'P2', 'P3', 'P4'],
          'Preço': [10.99, 4.99, 6.50, 8.75],
          'Quantidade Vendida': [100, 200, 150, 75]}

df_vendas = pd.DataFrame(vendas)

# imprime as informações do dataframe
print(df_vendas.head())