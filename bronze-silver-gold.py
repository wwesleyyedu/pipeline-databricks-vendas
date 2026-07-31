# Databricks notebook source
# DBTITLE 1,Ler Arquivo com Spark
df = spark.read.csv(
    "/Volumes/workspace/default/catvendas/vendas.csv",
    header=True,
    inferSchema=True
)

display(df)

# COMMAND ----------

# DBTITLE 1,Verifica esquema
df.printSchema()

# COMMAND ----------

# DBTITLE 1,Criar Camada Bronze, Gravar dados brutos no formato Del ...
df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze_vendas")

# COMMAND ----------

# DBTITLE 1,Consulta camada bronze SQL
# MAGIC %sql
# MAGIC SELECT * FROM bronze_vendas

# COMMAND ----------

# DBTITLE 1,Transformação Silver
from pyspark.sql.functions import col

silver_df = (
    df.withColumn(
        "valor_total",
        col("quantidade") * col("preco_unitario")
    )
)

# COMMAND ----------

# DBTITLE 1,Vizualiza
display(silver_df)

# COMMAND ----------

# DBTITLE 1,Salvar
silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver_vendas")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Na camada gold vamos gerar métricas de negócio.
# MAGIC #### Faturamento por categoria:
# MAGIC

# COMMAND ----------

# DBTITLE 1,Criar Camada Gold
from pyspark.sql.functions import sum

gold_df = (
    silver_df.groupBy("categoria")
    .agg(
        sum("valor_total")
        .alias("faturamento_total")
    )
)

# COMMAND ----------

# DBTITLE 1,Visualizar
display(gold_df)

# COMMAND ----------

# DBTITLE 1,Salvar
gold_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold_faturamento_categoria")

# COMMAND ----------

# DBTITLE 1,Consulta SQL
# MAGIC %sql
# MAGIC SELECT
# MAGIC     categoria,
# MAGIC     faturamento_total
# MAGIC FROM gold_faturamento_categoria
# MAGIC ORDER BY faturamento_total DESC;