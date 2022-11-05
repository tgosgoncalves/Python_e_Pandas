import pandas as pd


df = pd.read_csv("C:\\Users\\Ninha\\Desktop\\Geração Tech Unimed - BH - Ciencia de Dados\\Python_pandas\\datasets\\Gapminder.csv", error_bad_lines = False, sep = ";" )


print(df.head())


df = df.rename(columns = {"country":"Pais", "continent":"Continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap":"PIB"})
print(df.head())                                        


print(df.shape)


print(df.dtypes)


print(df.tail())


print(df.describe())


print(df["Continente"].unique())                         

Oceania = df.loc[df["Continente"] == "Oceania"]         
print(Oceania.head())

print(Oceania["Continente"].unique())


print(df.groupby("Continente")["Pais"].nunique())       


print(df.groupby("Ano")["Expectativa de vida"].mean()) 