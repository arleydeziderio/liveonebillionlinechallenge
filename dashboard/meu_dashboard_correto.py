import streamlit as st
import duckdb
import pandas as pd

# Função para carregar dados do arquivo Parquet
def load_data():
    con = duckdb.connect()
    df = con.execute(" SELECT * FROM 'data/measurements_summary.parquet'").df()
    con.close()
    return df

# Função principal para criar o dashboard
def main():
    st.title("Resumo de Temperatura por Cidades")