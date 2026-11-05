#%% 
import pandas as pd 

import os
import pandas as pd

# Defina o caminho para a pasta onde os arquivos estão salvos 

caminho_pasta = r"C:\Users\nanda\OneDrive\Desktop\pandas\ipea" 

# Lista com todos os arquivos CSV 
arquivos = [
    "homicidio-de-jovens-por-armas-de-fogo.csv",
    "homicidios-de-homens-por-armas-de-fogo.csv",
    "homicidios-de-jovens-homens.csv",
    "homicidios-de-jovens-mulheres.csv",
    "homicidios-de-jovens.csv",
    "homicidios-de-mulheres-por-armas-de-fogo.csv",
    "homicidios-homens-nao-negros.csv",
    "homicidios-homens-negros.csv",
    "homicidios-homens.csv",
    "homicidios-mulheres-nao-negros.csv",
    "homicidios-mulheres-negras.csv",
    "homicidios-mulheres.csv",
    "homicidios-nao-negros.csv",
    "homicidios-negros.csv",
    "homicidios-por-armas-de-fogo.csv",
    "homicidios.csv"
]

lista_dfs = []

for arquivo in arquivos:
    caminho_completo = os.path.join(caminho_pasta, arquivo)
    
    if os.path.exists(caminho_completo):
        try:
            
            df = pd.read_csv(caminho_completo,sep=";", encoding='utf-8')
            
            # Cria uma coluna para identificar a origem/categoria dos dados
            df['categoria'] = arquivo.replace('.csv', '')
            
            lista_dfs.append(df)
        except Exception as e:
            print(f"Erro ao ler o arquivo {arquivo}: {e}")
    else:
        print(f"Arquivo não encontrado: {caminho_completo}")

# Junta todos os dataframes em um só (empilhamento vertical)
if lista_dfs:
    df_final = pd.concat(lista_dfs, ignore_index=True)
    print("DataFrame combinado com sucesso!")
    print(f"Total de linhas: {df_final.shape[0]}, Total de colunas: {df_final.shape[1]}")
    
    # Salvar o resultado consolidado em um novo arquivo CSV
    df_final.to_csv("homicidios_consolidado.csv", index=False, encoding='utf-8-sig')
else:
    print("Nenhum arquivo foi carregado.")
# %%
