import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_excel("C:\\Users\\Ninha\\Desktop\\Geração Tech Unimed - BH - Ciencia de Dados\\Python_pandas\\datasets\\Aracaju.xlsx")   # Se der erro de leitura/carregamento usar engine="openpyxl"
df2 = pd.read_excel("C:\\Users\\Ninha\\Desktop\\Geração Tech Unimed - BH - Ciencia de Dados\\Python_pandas\\datasets\\Fortaleza.xlsx") # Se der erro de leitura/carregamento usar engine="openpyxl"
df3 = pd.read_excel("C:\\Users\\Ninha\\Desktop\\Geração Tech Unimed - BH - Ciencia de Dados\\Python_pandas\\datasets\\Natal.xlsx")     # Se der erro de leitura/carregamento usar engine="openpyxl"
df4 = pd.read_excel("C:\\Users\\Ninha\\Desktop\\Geração Tech Unimed - BH - Ciencia de Dados\\Python_pandas\\datasets\\Recife.xlsx")    # Se der erro de leitura/carregamento usar engine="openpyxl"
df5 = pd.read_excel("C:\\Users\\Ninha\\Desktop\\Geração Tech Unimed - BH - Ciencia de Dados\\Python_pandas\\datasets\\Salvador.xlsx")  # Se der erro de leitura/carregamento usar engine="openpyxl"

df = pd.concat([df1, df2, df3, df4, df5])

print(df.head())
print(df.tail())

print(df4.head())

(print(df.sample(5)))


print(df.dtypes)                                       

df["LojaID"] = df["LojaID"].astype("object")
print(df.dtypes)

print(df.isnull().sum())


print(df["Vendas"].mean())                                  
df["Vendas"].fillna(df["Vendas"].mean(), inplace = True)    


df["Vendas"].fillna(0, inplace = True)                     


df.dropna(inplace = True)                                   


df.dropna(how = "all", inplace = True)


df["Receita"] = df["Vendas"].mul(df["Qtde"])                
print(df.head())


print(df["Receita"].max())
print(df["Receita"].min())


print(df.nlargest(3, "Receita"))
print(df.nsmallest(3, "Receita"))


print(df.groupby("Cidade")["Receita"].sum())                


print(df.sort_values("Receita", ascending = False).head(10))


df["Data"] = df["Data"].astype("int64")


print(df.dtypes)


df["Data"] = pd.to_datetime(df["Data"])                     
print(df.dtypes)


df.groupby(df["Data"].dt.year)["Receita"].sum ()              
print(df.groupby(df["Data"].dt.year)["Receita"].sum())


df["Ano_Venda"] = df["Data"].dt.year
print(df.sample(5))


df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)         
print(df.sample(5))


df["Data"].min()                                            
print(df["Data"].min())


df["diferenca_dias"] = df["Data"] - df["Data"].min()
print(df.sample(5))


df["trimestre_venda"] = df["Data"].dt.quarter               
print(df.sample(5))


vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
print(vendas_marco_19)
print(vendas_marco_19.sample(20))


df["LojaID"].value_counts(ascending = False)               
print(df["LojaID"].value_counts(ascending = False))


df["LojaID"].value_counts(ascending = False).plot.bar()
plt.show()


df["LojaID"].value_counts(ascending = False).plot.barh()    
plt.show()                                                  


df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()
plt.show()


df["Cidade"].value_counts()                                                          


df["Cidade"].value_counts().plot.bar(title ="Total de vendas por cidade")
plt.xlabel("Cidade")                                                                 
plt.ylabel("Total de Vendas")                                                        
plt.show()


df["Cidade"].value_counts().plot.bar(title ="Total de vendas por cidade", color = "red")
plt.xlabel("Cidade")                                                                 
plt.ylabel("Total de Vendas")                                                        
plt.show()


plt.style.use("ggplot")                                                              
df.groupby(df["mes_venda"])["Qtde"].sum().plot(title ="Total de vendas por cidade", color = "red")
plt.xlabel("Mês")                                                                 
plt.ylabel("Total de Produtos Vendidos")  
plt.legend()                                        
plt.show()

print(df.groupby(df["mes_venda"])["Qtde"].sum())


df_2019 = df[df["Ano_Venda"] == 2019]
print(df_2019)


df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")               
plt.xlabel("Mês")                                                                 
plt.ylabel("Total de Produtos Vendidos")  
plt.legend()                                        
plt.show()


plt.hist(df["Qtde"], color = "magenta")                                              
plt.show()


plt.scatter(x = df_2019["dia_venda"], y = df_2019["Receita"])
plt.show()


df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total de produtos vendidos")
plt.legend()
plt.savefig("grafico QTDE x MES.png")
plt.show()