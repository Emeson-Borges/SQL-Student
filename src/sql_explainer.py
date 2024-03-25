import re

import streamlit as st


def explain_sql_commands(query):
    st.subheader('Explicação dos Principais Comandos SQL:')
    commands = {
    'SELECT': 'Utilizado para recuperar dados de uma ou mais tabelas.',
    'INSERT': 'Utilizado para adicionar novos registros a uma tabela.',
    'UPDATE': 'Utilizado para atualizar os valores de uma ou mais colunas em registros existentes.',
    'DELETE': 'Utilizado para excluir registros de uma tabela.',
    'FROM': 'Especifica de qual tabela ou tabelas os dados serão recuperados.',
    'WHERE': 'Filtra os registros com base em uma condição específica.',
    'JOIN': 'Combina colunas de duas ou mais tabelas com base em uma condição relacionada.',
    'GROUP BY': 'Agrupa os resultados de uma consulta por um ou mais campos.',
    'ORDER BY': 'Ordena os resultados da consulta.',
    'COUNT': 'Retorna o número de linhas que atendem a uma condição especificada.',
    'HAVING': 'Filtrar os resultados de uma consulta que envolve uma função de agregação.',
    'DISTINCT': 'Seleciona apenas valores únicos de uma coluna.',
    'AS': 'Renomeia uma coluna ou tabela em uma consulta.',
    'UNION': 'Combina o resultado de duas ou mais consultas em uma única tabela de resultados.',
    'INTERSECT': 'Retorna os registros que são comuns às duas consultas.',
    'EXCEPT': 'Retorna os registros que aparecem na primeira consulta e não na segunda consulta.',
    'LIMIT': 'Limita o número de linhas retornadas em uma consulta.',
    'OFFSET': 'Pula um número específico de linhas no início de um conjunto de resultados.',
    'BETWEEN': 'Filtrar os resultados com base em um intervalo de valores.',
    'LIKE': 'Filtrar os resultados com base em um padrão de texto.',
    'IN': 'Filtrar os resultados com base em uma lista de valores.',
    'NOT': 'Negar uma condição.',
    'NULL': 'Representa um valor nulo em um campo de dados.',
    'AND': 'Operador lógico que retorna verdadeiro se todas as condições forem verdadeiras.',
    'OR': 'Operador lógico que retorna verdadeiro se pelo menos uma das condições for verdadeira.',
    'CASE': 'Implementar lógica condicional em uma consulta SQL.',
    'JOIN': 'Combina colunas de duas ou mais tabelas com base em uma condição relacionada.',
    'LEFT JOIN': 'Retorna todos os registros da tabela à esquerda e os registros correspondentes da tabela à direita.',
    'RIGHT JOIN': 'Retorna todos os registros da tabela à direita e os registros correspondentes da tabela à esquerda.',
    'FULL JOIN': 'Retorna todos os registros quando houver uma correspondência em uma das tabelas.',
    'INNER JOIN': 'Retorna os registros quando houver pelo menos uma correspondência em ambas as tabelas.',
    'CROSS JOIN': 'Retorna o produto cartesiano de duas tabelas, isto é, todas as combinações de linhas de ambas as tabelas.',
    'NATURAL JOIN': 'Faz um join entre duas tabelas com base em todas as colunas que têm o mesmo nome em ambas as tabelas.',
    'CREATE TABLE': 'Cria uma nova tabela no banco de dados.',
    'ALTER TABLE': 'Altera a estrutura de uma tabela existente.',
    'DROP TABLE': 'Exclui uma tabela existente do banco de dados.',
    'CREATE INDEX': 'Cria um índice em uma tabela.',
    'DROP INDEX': 'Exclui um índice existente.',
    'TRUNCATE TABLE': 'Exclui todos os registros de uma tabela, mas mantém a estrutura da tabela.',
    'BEGIN': 'Inicia uma transação.',
    'COMMIT': 'Confirma as alterações feitas em uma transação.',
    'ROLLBACK': 'Desfaz as alterações feitas em uma transação.',
    'GRANT': 'Concede privilégios de acesso a usuários ou funções.',
    'REVOKE': 'Revoga privilégios de acesso concedidos anteriormente.',
    'CREATE USER': 'Cria um novo usuário no banco de dados.',
    'DROP USER': 'Exclui um usuário existente do banco de dados.',
    'CREATE DATABASE': 'Cria um novo banco de dados.',
    'DROP DATABASE': 'Exclui um banco de dados existente.',
    'USE': 'Seleciona um banco de dados específico para trabalhar.',
    'SHOW DATABASES': 'Exibe todos os bancos de dados disponíveis no servidor.',
    'SHOW TABLES': 'Exibe todas as tabelas disponíveis no banco de dados atual.',
    'DESCRIBE': 'Fornece informações sobre a estrutura de uma tabela.',
    'EXPLAIN': 'Exibe informações sobre como o banco de dados executará uma consulta.',
    'SET': 'Configura uma variável de ambiente no banco de dados.'
}


    for command, explanation in commands.items():
        if re.search(r'\b{}\b'.format(command), query, re.IGNORECASE):
            st.markdown(f'- **{command}**: {explanation}')
