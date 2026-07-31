# Databricks notebook source
dados = [
    (1, "2026-01-10", "Notebook", "Informática", 2, 3500),
    (2, "2026-01-11", "Mouse", "Informática", 5, 80),
    (3, "2026-01-12", "Monitor", "Informática", 1, 1200),
    (4, "2026-01-12", "Cadeira", "Escritório", 3, 600),
    (5, "2026-01-13", "Teclado", "Informática", 4, 150),
    (6, "2026-01-14", "Mesa", "Escritório", 2, 900)
]

colunas = [
    "id_venda",
    "data",
    "produto",
    "categoria",
    "quantidade",
    "preco_unitario"
]

df = spark.createDataFrame(dados, colunas)

display(df)