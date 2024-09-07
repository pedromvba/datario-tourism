import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import pydeck as pdk


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