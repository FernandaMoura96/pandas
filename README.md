# 🐼 Pandas: Estudos Práticos para Análise de Dados

![Python](https://img.shields.io/badge/Python-3.13+-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?logo=visualstudiocode&logoColor=white)
![Status](https://img.shields.io/badge/status-finalizado-brightgreen)

Repositório que documenta minha jornada de estudos práticos com a biblioteca **Pandas**, do básico (Series e estatística descritiva) a técnicas aplicadas a problemas reais de negócio, como junção de bases (*merge/join*) e **projeção de faturas de cartão de crédito**.

O objetivo é consolidar, de forma organizada e reproduzível, as competências necessárias para a atuação como **Analista de Dados**.

---

## 📌 Sumário

- [Competências demonstradas](#-competências-demonstradas)
- [Destaque: projeção de faturas de cartão de crédito](#-destaque-projeção-de-faturas-de-cartão-de-crédito)
- [Estrutura do repositório](#-estrutura-do-repositório)
- [Tecnologias](#-tecnologias)
- [Como executar](#-como-executar)
- [Autora](#-autora)

---

## 🎯 Competências demonstradas

| Área | O que foi praticado |
|---|---|
| **Estruturas de dados** | `pd.Series`, `pd.DataFrame`, índices e tipos de dados |
| **Estatística descritiva** | `.mean()`, `.var()`, `.describe()` |
| **Leitura e tratamento** | `pd.read_csv`, conversão de tipos com `pd.to_datetime`, criação de colunas derivadas |
| **Combinação de bases** | Junção de tabelas com `merge` / `join` |
| **Transformação de dados** | `explode`, `apply`, `groupby`, `pivot` (de formato "largo" para "longo" e vice-versa) |
| **Séries temporais** | Projeção de datas com `pd.DateOffset` |

---

## 💳 Destaque: projeção de faturas de cartão de crédito

### Contexto de negócio

Quando um cliente parcela uma compra, a base de transações registra apenas o **valor total** e a **quantidade de parcelas**. Porém, para áreas de crédito, cobrança e planejamento financeiro, a pergunta relevante é outra:

> *"Quanto cada cliente terá de fatura em cada um dos próximos meses?"*

Este case simula esse cenário com **dados fictícios** e entrega uma visão mês a mês do valor projetado por cliente.

### Abordagem

1. **Cálculo da parcela:** valor da venda ÷ quantidade de parcelas.
2. **Expansão das compras:** cada transação vira várias linhas, uma por parcela, com `explode`.
3. **Projeção do vencimento:** soma de meses à data da transação com `pd.DateOffset`.
4. **Consolidação:** agrupamento por cliente e mês, somando todas as parcelas que caem na mesma fatura.
5. **Visão final:** tabela dinâmica com clientes nas linhas e meses nas colunas.

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
