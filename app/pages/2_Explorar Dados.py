import streamlit as st
import os
import pandas as pd


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

############ Q3 e Q9 #################
st.header('Exploração dos Dados')

st.subheader('Filtragem dos Dados')

uploaded_path = './data/03_uploaded/uploaded_file.csv'

if not os.path.isfile(uploaded_path):
    st.write('Antes de explorar os dados, favor inserir seu arquivo na aba Introdução')

else:
    st.write('Identificamos o seu upload. Seguem seus dados para exploração')
    df = pd.read_csv(uploaded_path, encoding='utf-8')
    st.dataframe(df)

    st.write('Deseja realizar a análise por continente ou país?')
    group = st.radio(
        'Escolha Continente ou País',
        options=['Continente', 'País']
    )

    if group == 'País':
        selection = st.multiselect(
            'Filtre os Dados por Países',
            options=df['Pais'].unique())
        filtered_df = df[df['Pais'].isin(selection)]
    
    else:
        selection = st.multiselect(
            'Filtre os Dados por Contiente',
            options=df['Continente'].unique())
        filtered_df = df[df['Continente'].isin(selection)]
    
    if not filtered_df.empty:
        st.dataframe(filtered_df)

############ Q4 ######################
        st.subheader('Download dos Dados Filtrados')
        st.download_button(
            label='Caso deseje exportar os dados filtrados em formato .csv, favor utilizar o botão abaixo',
            data=filtered_df.to_csv(index=False, encoding='utf-8'),
            file_name='dados_filtrados.csv'
            )

############ Q10 e Q11 #################
        st.subheader('Análise Gráfica dos Dados')






