import pandas as pd

# base de dados
tab_vendas = pd.read_excel("Vendas.xlsx")

#visualizar a base de dados

pd.set_option('display.max_columns', None)
print(tab_vendas)

#faturamento por loja
faturamento = tab_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
print(faturamento)

# quantidade de produtos vendidos por loja
quantidade = tab_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
print(quantidade)

#ticket médio de cada loja
ticket_medio = (faturamento["Valor Final"] / quantidade["Quantidade"]).to_frame()
print(ticket_medio)

