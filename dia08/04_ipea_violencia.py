#%%
import pandas as pd 
import os 

def read_file(file_name:str):

    homicidios= (pd.read_csv(f"../ipea/{file_name}.csv", sep = ";")
            .rename(columns= 
                                        {"valor" : file_name
                                        ,"nome": "UF"})
            .set_index(["UF", "período"])
            .drop(["cod"], axis=1))
    return homicidios 


#%% 
file_names = os.listdir("../ipea")
dfs = []
for i in file_names:
    file_names = i.split(".")[0]
    dfs.append(read_file(file_names))


# %%
lista_geral = pd.concat(dfs,axis=1 ).reset_index().sort_values(['período',"UF"])
lista_geral
# %%
