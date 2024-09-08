import streamlit as st
import os
import shutil
import pandas as pd
import time

st.set_page_config(
    page_title="Introdução - Comece por Aqui",
    page_icon="👋",
)


# applying the backgroud color

background_color = st.session_state['backgroud_state']

st.markdown(
    f'''
    <style>
    [data-testid="stApp"] {{
        background-color: {background_color}
    }}
    </style>
    ''',
    unsafe_allow_html=True)





############ Q1 ######################
st.header('Introdução - Comece por Aqui 👋')

st.subheader('Objetivo e Motivação')
st.write('''
        O objetivo do dashboard é facilitar análises com relação a nacionalidade de turistas que chegaram no Rio de Janeiro,
        em determinado ano, por via aérea.

        A partir dessa análise será possível identificar públicos alvos para campanhas de turismo nos próximos anos uma vez que
        poderão ser visualizados de forma fácil os países que mais trazem turistas para o Rio de Janeiro, bem como a sazonalidade
        das visitas em um período anual, discretizado mensalmente. Os países envolvidos na análise são os das Américas do Norte e
        do Sul, devido a relevância e proximidade com a cidade do Rio de Janeiro.
         
        O Dashboard permitirá, dentre outras funcionalidades, que sejam visualizadas as variações mensais do fluxo de turistas por
        país e continente, bem como a distribuição por país dos turistas, facilitando assim a identificação de sazonalidades e e
        públicos alvo. Ainda, será possível verificar de forma rápida métricas como o total de turistas por mês, dentre outras.
        
         Por fim, o dashboard permitirá que, após o upload dos dados, insights sejam descobertos por meio de filtros e seletores.
         '''
)

############ Q2 e Q5 ######################
st.subheader('Upload dos Dados')

st.write('''
        Nesta seção é possível realizar o upload dos dados (somente um arquivo) para que seja o dashboard seja alimentado. Assim, antes de
        acessar as outras páginas, favor realizar o upload de um arquivo .csv no formato abaixo:

        | Continente       | País       | Mês         | Número de Visitantes  |  Lat    | Long     | Sigla
        |------------------|------------|-------------|-----------------------|---------|--------- |--------- |
        | América do Norte | Canadá     | Janeiro     | 1209                  | 56.1304 | -106.3468| CAN      |
        | América do Norte | Canadá     | Fevereiro   | 1496                  | 56.1304 | -106.3468| CAN      |
        | América do Norte | Canadá     | Março       | 1633                  | 56.1304 | -106.3468| CAN      |
        | América do Norte | Canadá     | Abril       | 722                   | 56.1304 | -106.3468| CAN      |
         


        Após inserir os dados, o dashboard já estará ativo e disponível para que seja realizada a análise.
         '''
)



uploaded_file = st.file_uploader(
                label='Favor inserir seu arquivo .csv aqui.',
                type='csv'
                )

if uploaded_file:

    df = pd.read_csv(uploaded_file, encoding='utf-8') 
    df.to_csv('./data/03_uploaded/uploaded_file.csv', index=False, encoding='utf-8')
    st.session_state['file_state'] = 1 # maintain the file without deletion

    progress_bar = st.progress(0, text='Estamos Processando os seus Dados!')
    for percent in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent + 1, text='Estamos Processando os seus Dados!')
    
    time.sleep(1)
    progress_bar.empty()


    time.sleep(0.3)
    st.write('Seguem abaixo as primeiras linhas dos dados recebidos. Favor acessar a aba Explorar Dados para iniciar sua análise.')
    st.dataframe(df.head())
