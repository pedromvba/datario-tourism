import streamlit as st
import os
import pandas as pd

# Q3
st.header('Exploração dos Dados')

uploaded_path = './data/03_uploaded/uploaded_file.csv'

if not os.path.isfile(uploaded_path):
    st.write('Antes de explorar os dados, favor inserir seu arquivo na aba Introdução')

else:
    st.write('Identificamos o seu upload. Segue amostra dos seus dados:')
    df = pd.read_csv(uploaded_path, encoding='utf-8')
    st.dataframe(df.head())

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