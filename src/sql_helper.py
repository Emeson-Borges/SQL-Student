import random

import psycopg2

from connection import connect


def execute_query(query):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()



def fetch_query(query):
    # Conectar ao banco de dados
    conn = psycopg2.connect(
        host="localhost",
        database="SQL-Student",
        user="postgres",
        password="161213"
    )
    
    # Abrir um cursor para executar consultas
    cur = conn.cursor()

    # Executar a consulta SQL
    cur.execute(query)
    
    # Obter os dados da consulta
    rows = cur.fetchall()

    # Fechar o cursor e a conexão com o banco de dados
    cur.close()
    conn.close()
    
    # Retornar os resultados como uma lista de dicionários
    col_names = [desc[0] for desc in cur.description]
    result = [dict(zip(col_names, row)) for row in rows]
    return result


def get_random_hint():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, pergunta, resposta FROM desafios ORDER BY RANDOM() LIMIT 1;")
        hint = cursor.fetchone()
        conn.close()
        return hint
    except psycopg2.Error as e:
        return f"Erro ao obter a dica: {e}"