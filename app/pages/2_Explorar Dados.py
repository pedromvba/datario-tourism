import os
import time
import streamlit as st
import pandas as pd
import geopandas as gpd
from services.plots import bar_plot, line_plot, area_plot, geo_plot

################## Q7 #######################
# Reading Data Function
@st.cache_data
def read_data(path):
    return pd.read_csv(path, encoding='utf-8')

@st.cache_data
def read_map(map_path):
    return gpd.read_file(map_path)


# applying the backgroud color using the session state
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

UPLOADED_PATH = './data/03_uploaded/uploaded_file.csv'

# does not let the user work on this page before uploading his data
if not os.path.isfile(UPLOADED_PATH):
    st.write('Antes de explorar os dados, favor inserir seu arquivo na aba Introdução')

else: # if the file exists
    st.write('Identificamos o seu upload. Seguem seus dados para exploração')

    df = read_data(UPLOADED_PATH)
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

        # creating metrics
        metrics_df = filtered_df
        filtered_visitors = metrics_df['Numero de Visitantes'].sum()
        grouped_df = metrics_df.groupby('Pais')['Numero de Visitantes'].sum()
     
    else:
        selection = st.multiselect(
            'Filtre os Dados por Contiente',
            options=df['Continente'].unique())
        
        filtered_df = df[df['Continente'].isin(selection)]

        # creating metrics
        metrics_df = filtered_df
        filtered_visitors = metrics_df['Numero de Visitantes'].sum()
        grouped_df = metrics_df.groupby('Continente')['Numero de Visitantes'].sum()


    if not filtered_df.empty: # plotting the graphs only after selection was made by the user

############ Q5 #################
        # spinner
        with st.spinner('Estamos Plotando os Gráficos e Calculando as Métricas, Por Favor Aguarde'):
            time.sleep(2)
            st.success('Pronto!')


        st.dataframe(filtered_df)
        st.write('_________________')


############ Q10, Q11 e Q12 #################
        st.subheader(' Métricas e Análise Gráfica dos Dados')

################## Metrics #######################    
        st.write('#### 1. Métrica Absoluta Perante o Total dos Dados')

        # calculating absolute metric
        total_visitors = df['Numero de Visitantes'].sum()
        selected_visitors_pct = round(100*(filtered_visitors/total_visitors),2)

        col1, col2 = st.columns(2)
        col1.metric('Número de Turistas Selecionados', filtered_visitors)
        col2.metric('Percentual do Total', f'{selected_visitors_pct}%')

        # calculating relative metric
        st.write('#### 2. Métricas Relativa à Seleção Realizada')

        # calculating metric for each selection of the user
        for i in range(grouped_df.shape[0]):
            country_percent = grouped_df.iloc[i] / filtered_visitors
            country = grouped_df.index[i]

            st.metric(f'Percentual de {country} na seleção', f"{country_percent:.2%}")
        st.write('_________________')


################## Bar Plot #######################
        st.write('#### Distribuição Anual por País')
        # prepping the data
        barplot_df = filtered_df.groupby('Pais')['Numero de Visitantes'].sum().reset_index().sort_values(by='Numero de Visitantes', ascending=False )

        bar_plot(barplot_df)

################## Geo Plot #######################

        # loading the shape file into a geopandas dataframe
        MAP_PATH = './data/01_raw/geoBoundariesCGAZ_ADM0.shp'
        world_map = read_map(MAP_PATH)

        # grouping data by visitantes e sigla
        map_grouped_df = filtered_df.groupby(['Pais', 'Sigla'], as_index=False).agg({'Numero de Visitantes': 'sum'})

        # merging the dataframes to obtain one with the geometry, the country code, the name in portuguese and the number of visitors.
        merged_df = pd.merge(world_map, map_grouped_df, left_on='shapeGroup', right_on='Sigla', how='inner')

        geo_plot(merged_df)
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



