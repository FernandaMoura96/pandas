#%%

import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")

#%%

clientes = pd.read_sql_table(table_name= "tb_customers", con= engine)

clientes.shape
# %%

query = "SELECT * FROM tb_customers LIMIT  1000 "

df1000 =pd.read_sql_query( query , con = engine )
df1000
# %%


