#%%
import pandas as pd


idades = [22, 45, 18, 31, 60, 27, 42, 19, 55, 36, 24, 50, 65, 29, 33]



sr_idades = pd.Series(idades)

print(sr_idades)


media_idades = sr_idades.mean()

var_idades = sr_idades.var()

summary_idades = sr_idades.describe()

print(media_idades )
print(var_idades)
print(summary_idades)

'''Acessar o primeiro elemento de uma série,é igaul acessar na lista mas para acessar os outros segue-se o valor do indice '''

print(f'O primeiro da lista é {idades[0]} ')

print(f'O ultimo da lista é {sr_idades.iloc[-1]}')

print(f'Os tres primeiros da  lista são  {sr_idades.iloc[:3]}')



# %%
indexs  = [
    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
    "Fernanda", "Gabriel", "Helena", "Igor", "Julia",
    "Lucas", "Mariana", "Neto", "Olivia", "Pedro"
]
idades = [22, 45, 18, 31, 60, 27, 42, 19, 55, 36, 24, 50, 65, 29, 33]
sr_idades = pd.Series(idades, index = indexs)

print(sr_idades)
'''Agora é possivel acessar o valor com a posição dos nomes, 
o .iloc ignora o index '''
