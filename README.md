# 🐼 Pandas: Estudos Práticos para Análise de Dados

Repositório para documentar minha evolução com a biblioteca **Pandas**, organizado em dias de estudo. Cada pasta reúne os scripts e os exercícios daquele dia, com foco em manipulação, transformação e análise de dados tabulares.

> 🎯 **Objetivo:** consolidar a base técnica para atuar como Analista de Dados, trazendo para o Python a lógica que já uso em SQL e na rotina comercial.

---

## 🛠️ Tecnologias

| Item | Detalhe |
|------|---------|
| Linguagem | Python 3.13+ |
| Biblioteca principal | Pandas |
| Ambiente | VS Code (modo interativo, células `# %%`) |
| Versionamento | Git e GitHub |

---

## 📁 Estrutura do repositório

```
pandas/
├── data/        # Bases de dados utilizadas nos exercícios
├── dia01/       # Séries e estatística descritiva
├── dia02/       # Métodos e Colunas 
├── dia03/       # .copy()
├── dia04/       # Ordenação de colunas 
├── dia05/       # Eliminando Duplicatas 
├── dia06/       # .apply()
├── dia07/       # Groupby
├── dia08/       # Merge
├── dia09/       # Conexão com banco de dados
├── dia10/       # Stack/Unstack/Pivot/Explode
├── ipea         # Base de dados utilizada nos exercícios
└── README.md

---

## 📚 Conteúdos abordados

### Estruturas de dados
- `pd.Series` com índices personalizados
- `pd.DataFrame` e leitura de arquivos

### Estatística descritiva
- `.mean()`, `.var()` e `.describe()`

### Junção de tabelas (`merge`)
Cruzamento de transações, produtos e clientes para responder: *qual cliente mais realizou transações com o produto "Presença Streak"?* Compare as duas abordagens:

**1. Juntar tudo e filtrar depois**
```python
df_full = cliente_transacao_produto.merge(produto, on="IdProduto")
df_full = df_full[df_full["DescNomeProduto"] == "Presença Streak"]

(df_full.groupby(by=["IdCliente"])["IdTransacao"]
    .count()
    .sort_values(ascending=False)
    .head(1))

```

### Equivalência com SQL

| SQL | Pandas |
|-----|--------|
| `JOIN` | `merge()` |
| `WHERE` | filtro booleano `df[df["col"] == valor]` |
| `GROUP BY` | `groupby()` |
| `COUNT()` | `.count()` |
| `ORDER BY` | `sort_values()` |
| `LIMIT` | `head()` |

---

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/FernandaMoura96/pandas.git
   cd pandas
   ```

2. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # Windows: .venv\Scripts\activate
   ```

3. Instale a dependência:
   ```bash
   pip install pandas
   ```

4. Abra a pasta no VS Code e execute os arquivos `.py` célula por célula (`# %%`) no modo interativo.

---

## 👩‍💻 Autora

**Fernanda Moura**
Profissional com 15 anos de experiência em operações comerciais, em transição para Análise de Dados.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-fernanda--moura96-0A66C2?logo=linkedin&logoColor=white)](https://linkedin.com/in/fernanda-moura96)
[![GitHub](https://img.shields.io/badge/GitHub-FernandaMoura96-181717?logo=github&logoColor=white)](https://github.com/FernandaMoura96)
