import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import pydeck as pdk
import plotly.express as px
from services.plots import bar_plot, map_plot, line_plot, area_plot



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
st.header('Exploração dos Dados 🕵🏼')

st.subheader('Filtragem dos Dados')

uploaded_path = './data/03_uploaded/uploaded_file.csv'

if not os.path.isfile(uploaded_path):
    st.write('Antes de explorar os dados, favor inserir seu arquivo na aba Introdução')

else:
    st.write('Identificamos o seu upload. Seguem seus dados para exploração')
    df = pd.read_csv(uploaded_path, encoding='utf-8')
    st.dataframe(df)

    st.write('''
             Deseja realizar a análise por continente ou país? 
             
             Caso deseje uma análise geral dos dados, basta selecionar Continentes > America do Norte + América do Sul ''')
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
        st.write('_________________')


############ Q4 ######################
        st.subheader('Download dos Dados Filtrados')
        st.download_button(
            label='Caso deseje exportar os dados filtrados em formato .csv, favor clicar neste botão',
            data=filtered_df.to_csv(index=False, encoding='utf-8'),
            file_name='dados_filtrados.csv'
            )

        st.write('_________________')

############ Q10, Q11 e Q12 #################
        st.subheader('Análise Gráfica dos Dados')
        st.write('#### Distribuição Anual por País')

################## Bar Plot #######################
        # prepping the data
        barplot_df = filtered_df.groupby('Pais')['Numero de Visitantes'].sum().reset_index().sort_values(by='Numero de Visitantes', ascending=False )

        bar_plot(barplot_df)

################## Map Plot #######################

        grouped_df = filtered_df.groupby(['Pais', 'Lat', 'Long'], as_index=False).agg({'Numero de Visitantes': 'sum'})
        max_visitors = grouped_df['Numero de Visitantes'].max()
        grouped_df['size'] = (grouped_df['Numero de Visitantes']/max_visitors)*2000000

        map_plot(grouped_df)
        st.write('_________________')

################## Line Plot #######################
        st.write('#### Evolução Mensal')

        # prepping the data
        months = filtered_df['Mes'].unique()

        line_plot(filtered_df, months=months)

################## Area Plot #######################
        area_plot(filtered_df, months=months)
        st.write('_________________')
