#%% 
import pandas as pd 
import sqlalchemy 
from sklearn import cluster

#importar a query 

with open("etl.sql") as open_file:
    query = open_file.read()
print(query)
# %%

# criar e definir qual a conexão com o .bd

engine =  sqlalchemy.create_engine("sqlite:///../data/olist.db")
df = pd.read_sql_query(query, con= engine)
df
# %%
#"analise" de cluster 

kmean = cluster.KMeans(n_clusters=4 )
kmean.fit(df[['totalRevenue', 'qtSalles']])
df["cluster"] = kmean.labels_
df
# %%
# devolvendo a tabela para o meu .db

df.to_sql('sellers_cluster', con=engine, index= False)
# %%
