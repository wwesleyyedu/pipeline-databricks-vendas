# 🚀 Pipeline ETL de Vendas com Databricks e PySpark

## 📋 Visão Geral

Este projeto demonstra a construção de um pipeline ETL utilizando Databricks Free Edition, PySpark e Delta Lake, seguindo a arquitetura Medallion (Bronze, Silver e Gold).

O pipeline realiza a ingestão de dados de vendas a partir de um arquivo CSV, executa transformações para enriquecimento dos dados e gera métricas analíticas para suporte à tomada de decisão.

---

## 🎯 Objetivo

Desenvolver um pipeline de dados completo utilizando tecnologias modernas de Engenharia de Dados, aplicando conceitos de:

- ETL
- Data Lakehouse
- Arquitetura Medallion
- Processamento distribuído com Spark
- Persistência em Delta Lake
- Análise de dados com SQL

---

## 🏗️ Arquitetura

```text
vendas.csv
    │
    ▼
┌─────────────┐
│   Bronze    │
│ Dados Brutos│
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Silver    │
│ Dados Trat. │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Gold     │
│ Métricas    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Dashboard   │
└─────────────┘
```

![Arquitetura](docs/arquitetura.png)

---

## 🛠️ Tecnologias Utilizadas

- Databricks Free Edition
- Apache Spark
- PySpark
- Delta Lake
- SQL
- Python
- Git
- GitHub

---

## 📂 Estrutura do Projeto

```text
pipeline-databricks-vendas/
│
├── data/
│   └── vendas.csv
│
├── notebooks/
│   ├── 01_ingestao.py
│   ├── 02_bronze.py
│   ├── 03_silver.py
│   └── 04_gold.py
│
├── sql/
│   └── consultas.sql
│
├── docs/
│   ├── bronze.png
│   ├── silver.png
│   ├── gold.png
│   └── dashboard.png
│
└── README.md
```

---

## 📥 Ingestão dos Dados

Os dados foram carregados a partir de um arquivo CSV utilizando PySpark.

### Exemplo

```python
df = spark.read.csv(
    "/Volumes/workspace/default/catvendas/vendas.csv",
    header=True,
    inferSchema=True
)
```

---

## 🥉 Camada Bronze

Armazenamento dos dados brutos sem transformações.

### Objetivos

- Preservar os dados originais
- Garantir rastreabilidade
- Permitir reprocessamento

```python
df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze_vendas")
```

![Bronze](docs/bronze.png)

---

## 🥈 Camada Silver

Tratamento e enriquecimento dos dados.

### Transformação Aplicada

Criação da coluna de faturamento total:

```python
from pyspark.sql.functions import col

silver_df = df.withColumn(
    "valor_total",
    col("quantidade") * col("preco_unitario")
)
```

### Resultado

![Silver](docs/silver.png)

---

## 🥇 Camada Gold

Criação de métricas para análise de negócio.

### Faturamento por Categoria

```python
from pyspark.sql.functions import sum

gold_df = (
    silver_df.groupBy("categoria")
    .agg(
        sum("valor_total")
        .alias("faturamento_total")
    )
)
```

### Resultado

![Gold](docs/gold.png)

---

## 📊 Consulta Analítica

```sql
SELECT
    categoria,
    faturamento_total
FROM gold_faturamento_categoria
ORDER BY faturamento_total DESC;
```

---

## 📈 Dashboard

Visualização dos resultados obtidos a partir da camada Gold.

Indicadores apresentados:

- Faturamento por categoria
- Comparativo de vendas
- Análise consolidada

![Dashboard](docs/dashboard.png)

---

## 🚀 Competências Demonstradas

- Engenharia de Dados
- Databricks
- Apache Spark
- PySpark
- SQL
- ETL
- ELT
- Delta Lake
- Data Lakehouse
- Data Transformation
- Data Analytics
- Git e GitHub

---

## 📚 Principais Aprendizados

- Leitura de arquivos CSV com Spark
- Manipulação de DataFrames
- Criação de pipelines ETL
- Arquitetura Bronze, Silver e Gold
- Persistência em Delta Lake
- Consultas analíticas com SQL
- Organização de projetos de Engenharia de Dados

---

## 👨‍💻 Autor

**Wesley**

Gerente de Contratos | Supervisor de Caldeiraria | Engenheiro de Software | Engenheiro de Segurança do Trabalho | Pós-Graduando em Engenharia de Dados e Inteligência Artificial

- LinkedIn: [www.linkedin.com/in/wesleyedu](https://www.linkedin.com/in/wesleyedu/)
- GitHub: [SEU_GITHUB](https://github.com/wwesleyyedu/pipeline-databricks-vendas)

---

## ⭐ Próximos Passos

- Ingestão de dados via API
- Automação de pipelines
- Apache Airflow
- dbt
- Azure Databricks
- Microsoft Fabric
- Processamento em Streaming
- Data Warehouse
