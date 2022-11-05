from tkinter import dialog
from turtle import title
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8")                        
pd.set_option('float_format', '{:20.2f}'.format)     


df = pd.read_excel("C:\\Users\\Ninha\\Desktop\\Geração Tech Unimed - BH - Ciencia de Dados\\Python_pandas\\datasets\\AdventureWorks.xlsx")


print(df.head())


print(df.shape)


print(df.dtypes)


print(df["Valor Venda"].sum())


df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"])        
print(df.head(1))                                               


round(df["Custo"].sum(), 2)                                     
print(round(df["Custo"].sum(), 2))                              


df["Lucro"] = df["Valor Venda"] - df["Custo"]
print(df.head(1))


round(df["Lucro"].sum(), 2)
print(round(df["Lucro"].sum(), 2))


df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]
print(df.head(1))


df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days   
print(df.head(1))


print(df["Tempo_envio"].dtype)


df.groupby("Marca")["Tempo_envio"].mean()
print(df.groupby("Marca")["Tempo_envio"].mean())       


df.isnull().sum()                                       
print(df.isnull().sum())                                


df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum()     

print(df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum())


lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index
print(lucro_ano)


df.groupby("Produto")["Quantidade"].sum().sort_values(ascending = False)            
print(df.groupby("Produto")["Quantidade"].sum().sort_values(ascending = False))


df.groupby("Produto")["Quantidade"].sum().sort_values(ascending = True).plot.barh(title = "Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto")
plt.show()            


df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title = "Lucro X Ano")
plt.xlabel("Ano")
plt.ylabel("Receita")
plt.show()

df.groupby(df["Data Venda"].dt.year)["Lucro"].sum()
print(df.groupby(df["Data Venda"].dt.year)["Lucro"].sum())


df_2009 = df[df["Data Venda"].dt.year == 2009]         
print(df_2009.head(5))


df_2009.groupby(df_2009["Data Venda"].dt.month)["Lucro"].sum().plot(title = "Lucro X Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro")
plt.show()


df_2009.groupby("Marca")["Lucro"].sum().plot.bar(title = "Lucro X Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation = "horizontal")                     
plt.show()


df_2009.groupby("Classe")["Lucro"].sum().plot.bar(title = "Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation = "horizontal")                     
plt.show()


df["Tempo_envio"].describe()
print(df["Tempo_envio"].describe())                     


plt.boxplot(df["Tempo_envio"])
plt.show()


plt.hist(df["Tempo_envio"])
plt.show()


df["Tempo_envio"].min()
print(df["Tempo_envio"].min())


df["Tempo_envio"].max()
print(df["Tempo_envio"].max())


df[df["Tempo_envio"] == 20]                             
print(df[df["Tempo_envio"] == 20])


df.to_csv("df_vendas_novo.csv", index = False)          
