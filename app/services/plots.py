import json
import streamlit as st
import pandas as pd
import altair as alt
import pydeck as pdk
import plotly.express as px

################## Bar Plot #######################
def bar_plot(df: pd.DataFrame) -> alt.Chart:
    '''
    Creates a horizontal bar chart using Altair to display the total number of visitors per country.

    :param df: DataFrame containing the visitor data, with 'Numero de Visitantes' and 'Pais' columns.
    :return: Altair chart displaying the number of visitors accumulated throughout the year by country.
    '''

    #plotting the chart
    chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Numero de Visitantes:Q', title='Número de Visitantes Anuais'),
    y=alt.Y('Pais:N', sort='-x', title='País'),
    color=alt.Color('Pais:N', legend=None),
    tooltip=[alt.Tooltip('Pais:N', title='País'),
            alt.Tooltip('Numero de Visitantes:Q', title='Número de Visitantes')]
).properties( # adjusting properties
    title='Número de Visitantes Acumulados no Ano por País',
    width=600,
    height=600
) 
    return st.altair_chart(chart, use_container_width=True)

################## Line Plot #######################
def line_plot(df: pd.DataFrame, months: list) -> alt.Chart:
    """
    Creates a line plot using Altair to display the monthly evolution of visitor arrivals by country.

    :param df: DataFrame containing the visitor data, with 'Mes', 'Numero de Visitantes', and 'Pais' columns.
    :param months: List of months in the correct order for sorting the x-axis.
    :return: Altair line chart showing the evolution of visitor arrivals by country over the months.
    """

    # plotting the chart
    lineplot = alt.Chart(df).mark_line(point=True).encode(
    x=alt.X('Mes:N', title='Mês', sort=months),
    y=alt.Y('Numero de Visitantes:Q', title='Número de Visitantes'),
    color=alt.Color('Pais:N', title='País'),
    tooltip=[alt.Tooltip('Pais:N', title='País'),
            alt.Tooltip('Mes:N', title='Mês'),
            alt.Tooltip('Numero de Visitantes:Q', title='Número de Visitantes')]
    ).properties(# adjusting properties
        title='Evolução Mensal da Chegada de Visitantes por País',
        width=800,
        height=600
    )
   
    return st.altair_chart(lineplot, use_container_width=True)


################## Area Plot #######################
def area_plot(df: pd.DataFrame, months: list) -> alt.Chart:
    """
    Creates an area chart using Altair to show the proportion of visitors throughout the year by country.

    :param df: DataFrame containing the visitor data, with 'Mes', 'Numero de Visitantes', and 'Pais' columns.
    :param months: List of months in the correct order for sorting the x-axis.
    :return: Altair area chart displaying the total number of visitors per country over the months.
    """

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

def geo_plot(df: pd.DataFrame):
    """
    Creates a choropleth map using Plotly to display the density of visitors by country.

    :param df: DataFrame containing the geographic data and visitor numbers, with columns like 'Numero de Visitantes', 'Sigla', and 'Pais'.
    :return: Plotly choropleth map.
    """

    # converting the geodataframe to geojson due to compatibility issues with plotly
    geojson_data = df.to_crs("EPSG:4326").to_json()

    # finding max and min values for the range of colors
    min_visitors = df['Numero de Visitantes'].min()
    max_visitors = df['Numero de Visitantes'].max()

    # creating the geo map
    fig = px.choropleth(
        df,
        geojson=json.loads(geojson_data),  #reading the data
        locations='Sigla',  # using Sigla as reference for the locations on the map
        featureidkey="properties.shapeGroup",  # field on the geojson that connect to the data
        color='Numero de Visitantes',  # column to define the color vatiation
        hover_name='Pais',  # tool tip
        color_continuous_scale='Blues',  # color scheme
        range_color=[min_visitors, max_visitors],  # range of color
        projection='mercator',  # type of projection
        width=1200,  # width of the image
        height=800   # height of the image
    )

    # limiting the area of them map that is shown
    fig.update_geos(
        visible=True,
        projection_type="mercator",
        lataxis=dict(range=[-60, 90]),
        lonaxis=dict(range=[-180, 0])
    )

    # Ajustar o layout do gráfico
    fig.update_layout(
        title_text='Densidade de Visitantes por País',
        title_x=0 # title to the left
    )

    # Mostrar o gráfico no Streamlit
    return st.plotly_chart(fig, use_container_width=True)
