import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import pydeck as pdk
import plotly.express as px
from services.plots import bar_plot, map_plot, line_plot, area_plot
import time


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

        metrics_df = filtered_df
        filtered_visitors = metrics_df['Numero de Visitantes'].sum()
        grouped_df = metrics_df.groupby('Pais')['Numero de Visitantes'].sum()

        
    else:
        selection = st.multiselect(
            'Filtre os Dados por Contiente',
            options=df['Continente'].unique())
        
        filtered_df = df[df['Continente'].isin(selection)]


        metrics_df = filtered_df
        filtered_visitors = metrics_df['Numero de Visitantes'].sum()
        grouped_df = metrics_df.groupby('Continente')['Numero de Visitantes'].sum()


    if not filtered_df.empty:
        st.dataframe(filtered_df)
        st.write('_________________')

############ Q5, Q10, Q11 e Q12 #################
        st.subheader(' Métricas e Análise Gráfica dos Dados')

        with st.spinner('Estamos Plotando os Gráficos e Calculando as Métricas'):
            time.sleep(1.5)
        st.success('Pronto!')

################## Metrics #######################

        total_visitors = df['Numero de Visitantes'].sum()
        selected_visitors_pct = round(100*(filtered_visitors/total_visitors),2)

        col1, col2 = st.columns(2)
        col1.metric('Número de Turistas Selecionados', filtered_visitors)
        col2.metric('Percentual do Total', selected_visitors_pct)
        st.write('_________________')


################## Bar Plot #######################
        st.write('#### Distribuição Anual por País')
        # prepping the data
        barplot_df = filtered_df.groupby('Pais')['Numero de Visitantes'].sum().reset_index().sort_values(by='Numero de Visitantes', ascending=False )

        bar_plot(barplot_df)

# Another Metrics
        for i in range(grouped_df.shape[0]):
            country_percent = grouped_df.iloc[i] / filtered_visitors
            country = grouped_df.index[i]

            st.metric(f'Percentual de {country} na seleção', f"{country_percent:.2%}")

################## Map Plot #######################

        map_grouped_df = filtered_df.groupby(['Pais', 'Lat', 'Long'], as_index=False).agg({'Numero de Visitantes': 'sum'})
        max_visitors = map_grouped_df['Numero de Visitantes'].max()
        map_grouped_df['size'] = (map_grouped_df['Numero de Visitantes']/max_visitors)*2000000

        map_plot(map_grouped_df)
        st.write('_________________')

################## Line Plot #######################
        st.write('#### Evolução Mensal')

        # prepping the data
        months = filtered_df['Mes'].unique()

        line_plot(filtered_df, months=months)

################## Area Plot #######################
        area_plot(filtered_df, months=months)
        st.write('_________________')

        ############ Q4 ######################
        st.subheader('Download dos Dados Filtrados')
        st.download_button(
            label='Caso deseje exportar os dados filtrados em formato .csv, favor clicar neste botão',
            data=filtered_df.to_csv(index=False, encoding='utf-8'),
            file_name='dados_filtrados.csv'
            )

        st.write('_________________')
