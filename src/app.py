import streamlit as st
from sql_explainer import explain_sql_commands
from sql_helper import fetch_query, get_random_hint
import difflib
import pandas as pd

def main():
    st.title('SQL Student Project')

    # Obter o estado atual da pergunta e da resposta correta
    estado = st.session_state.get('estado', {})
    pergunta_atual = estado.get('pergunta', '')
    resposta_correta_atual = estado.get('resposta', '')

    if not pergunta_atual:
        # Se não houver pergunta atual, obter uma nova pergunta
        desafio = get_random_hint()
        pergunta_atual = desafio[1]
        resposta_correta_atual = desafio[2]
        st.session_state['estado'] = {'pergunta': pergunta_atual, 'resposta': resposta_correta_atual}

    st.write('Questão:')
    st.write(pergunta_atual)  # Mostra a pergunta

    # Campo de entrada para a resposta do aluno
    resposta_aluno = st.text_input('Insira sua resposta:')

    # Botão para verificar a resposta do aluno
    if st.button('Verificar Resposta'):
        # Verificar se a resposta do aluno é semelhante à resposta correta
        if is_similar_answer(resposta_aluno, resposta_correta_atual):
            st.success('Resposta correta!')
            st.write('Resultado da consulta:')
            execute_query(resposta_correta_atual)
            
        else:
            st.error('Resposta incorreta. Tente novamente.')
        
        # Exibir explicação dos comandos SQL
        explain_sql_commands(resposta_aluno)

    # Botão para avançar para a próxima pergunta
    if st.button('Próxima Pergunta') or not pergunta_atual:
        st.session_state['estado'] = {}  # Limpar o estado atual para obter uma nova pergunta

def is_similar_answer(answer1, answer2):
    # Converter ambas as respostas para minúsculas e remover espaços em branco
    answer1 = answer1.strip().lower()
    answer2 = answer2.strip().lower()

    # Calcular a similaridade entre as respostas usando SequenceMatcher
    matcher = difflib.SequenceMatcher(None, answer1, answer2)
    similarity = matcher.ratio()

    # Se a similaridade for maior que um certo limite, consideramos as respostas como semelhantes
    similarity_threshold = 0.8  # Pode ajustar esse valor conforme necessário
    return similarity >= similarity_threshold

def execute_query(query):
    # Executar a consulta SQL do aluno e mostrar o resultado na tela
    rows = fetch_query(query)
    if rows:
        # Extrair os nomes das colunas do primeiro registro retornado
        col_names = list(rows[0].keys())
        # Converter o resultado em um DataFrame do Pandas para melhor exibição
        df = pd.DataFrame(rows, columns=col_names)
        st.write(df)
    else:
        st.write('Nenhum resultado encontrado.')

if __name__ == '__main__':
    main()
