import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import pydeck as pdk
import plotly.express as px
import json


################## Bar Plot #######################
def bar_plot(df):

    #plotting the chart
    chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Numero de Visitantes:Q', title='Número de Visitantes Anuais'),
    y=alt.Y('Pais:N', sort='-x', title='País'),
    color=alt.Color('Pais:N', legend=None),
    tooltip=[alt.Tooltip('Pais:N', title='País'), 
            alt.Tooltip('Numero de Visitantes:Q', title='Número de Visitantes')]
).properties(
    title='Número de Visitantes Acumulados no Ano por País',
    width=600,
    height=600
)
    
    return st.altair_chart(chart, use_container_width=True)


################## Map Plot #######################
def map_plot(df):

    layer = pdk.Layer(
                "ScatterplotLayer",
                data=df,
                get_position=['Long', 'Lat'],
                get_color="[255, 0, 0, 140]",
                get_radius="size", 
                radius_scale=1, 
                pickable=True,
                auto_highlight=True
            )

            
    view_state = pdk.ViewState(
                latitude=4.59808,
                longitude=-74.076044,
                zoom=2,
                pitch=0
            )

    deck = pdk.Deck(
                layers=[layer],
                initial_view_state=view_state,
                map_style="mapbox://styles/mapbox/light-v10",
                tooltip={
                    "text": "{Pais}\nNúmero de Visitantes: {Numero de Visitantes}"
                }
            )

    return st.pydeck_chart(deck)
    

################## Line Plot #######################
def line_plot(df, months):
    # plotting the chart
    lineplot = alt.Chart(df).mark_line(point=True).encode(
    x=alt.X('Mes:N', title='Mês', sort=months),
    y=alt.Y('Numero de Visitantes:Q', title='Número de Visitantes'),
    color=alt.Color('Pais:N', title='País'),
    tooltip=[alt.Tooltip('Pais:N', title='País'),
            alt.Tooltip('Mes:N', title='Mês'),
            alt.Tooltip('Numero de Visitantes:Q', title='Número de Visitantes')]
    ).properties(
        title='Evolução Mensal da Chegada de Visitantes por País',
        width=800,
        height=600
    )
    
    return st.altair_chart(lineplot, use_container_width=True)


################## Area Plot #######################
def area_plot(df, months):

    area_chart = alt.Chart(df).mark_area().encode(
        x=alt.X('Mes:N', title='Mês', sort=months),
        y=alt.Y('sum(Numero de Visitantes):Q', title='Número de Visitantes'),
        color=alt.Color('Pais:N', title='País'),
        tooltip=[alt.Tooltip('Pais:N', title='País'),
                alt.Tooltip('Mes:N', title='Mês'),
                alt.Tooltip('sum(Numero de Visitantes):Q', title='Número de Visitantes')]
    ).properties(
        title='Proporção de Visitantes ao Longo do Ano por País',
        width=800,
        height=400
    )

    return st.altair_chart(area_chart, use_container_width=True)



####################### Geo Plot ###############

def geo_plot(df):
            # Converter o GeoDataFrame para GeoJSON
        geojson_data = df.to_crs("EPSG:4326").to_json()

        # Encontrar o valor mínimo e máximo de visitantes
        min_visitors = df['Numero de Visitantes'].min()
        max_visitors = df['Numero de Visitantes'].max()

        # Criar o mapa coroplético com Plotly Express
        fig = px.choropleth(
            df,
            geojson=json.loads(geojson_data),  # Converter o GeoJSON em um formato legível para Plotly
            locations='Sigla',  # Usar a coluna 'Sigla' para relacionar os dados com as geometrias
            featureidkey="properties.shapeGroup",  # Identificar o campo que conecta o geojson com os dados
            color='Numero de Visitantes',  # Coluna para definir a intensidade das cores
            hover_name='Pais',  # Nome do país ao passar o mouse
            color_continuous_scale='Blues',  # Esquema de cores
            range_color=[min_visitors, max_visitors],  # Definir o intervalo de cor baseado nos valores de visitantes
            projection='mercator',  # Projeção mercator para ajuste mais específico
            width=1200,  # Definir a largura da figura
            height=800   # Definir a altura da figura
        )

        # Atualizar o layout do gráfico para limitar a latitude e longitude
        fig.update_geos(
            visible=True,
            projection_type="mercator",
            lataxis=dict(range=[-60, 90]),  # Limitar a latitude para mostrar o hemisfério ocidental
            lonaxis=dict(range=[-180, 0])  # Limitar a longitude para mostrar apenas o hemisfério ocidental
        )

        # Ajustar o layout do gráfico
        fig.update_layout(
            title_text="Número de Visitantes por País",
            title_x=0.5
        )

        # Mostrar o gráfico no Streamlit
        st.plotly_chart(fig, use_container_width=True)
