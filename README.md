# README

## Objetivo do Projeto

O objetivo do dashboard é facilitar análises com relação a nacionalidade de turistas que chegaram no Rio de Janeiro, em determinado ano, por via aérea.

A partir dessa análise será possível identificar públicos alvos para campanhas de turismo nos próximos anos uma vez que
poderão ser visualizados de forma fácil os países que mais trazem turistas para o Rio de Janeiro, bem como a sazonalidade
das visitas em um período anual, discretizado mensalmente. Os países envolvidos na análise são os das Américas do Norte e
do Sul, devido a relevância e proximidade com a cidade do Rio de Janeiro.
    
O Dashboard permitirá, dentre outras funcionalidades, que sejam visualizadas as variações mensais do fluxo de turistas por
país e continente, bem como a distribuição por país dos turistas, facilitando assim a identificação de sazonalidades e e
públicos alvo. Ainda, será possível verificar de forma rápida métricas como o total de turistas por mês, dentre outras.

Por fim, o dashboard permitirá que, após o upload dos dados, insights sejam descobertos por meio de filtros, seletores e gráficos.

## Instalação do Ambiente e Biblioteca

As dependências necessárias para a execução do projeto estão registradas no arquivo requirements.txt e a versão do Python utilizada foi a 3.12.4.


## Github do Projeto

[Link do Projeto - Data Tourism](https://github.com/pedromvba/datario-tourism)

## Dados do Projeto

Todas as pastas necessárias estão replicadas no GitHub. O único arquivo que não se encontra no GitHub é o arquivo *geoBoundariesCGAZ_ADM0.shp* que contém as geometrias/shapes dos países para compor o choropleth map. Esse arquivo pode ser baixado em [Link do Arquivo Shapes ](https://drive.google.com/file/d/18AY4qlMwTyxrL_qfYZ5DHdfIpyo3Fzfy/view?usp=share_link). Após baixar esse arquivo, o mesmo deve ser inserido na pasta /data/01_raw para o correto funcionamento do projeto.

O dado original foi obtido diretamente do site do [Data Rio](https://www.data.rio/search?groupIds=729990e9fbc04c6ebf81715ab438cae8), da área de Turismo. O dataset utilizado foi o [Chegada mensal de turistas pelo Rio de Janeiro, por via Aérea, segundo continentes e países de residência permanente, entre 2006-2019](https://www.data.rio/documents/a6c6c3ff7d1947a99648494e0745046d/about). Para este projeto em específico foram selecionados os dados referentes ao ano de 2019. Esses dados após tratamento, foram incluídos na pasta /data/02_processed.

Para o tratamento, foi utilizada a ferramenta do Chat-GPT que auxiliou o desenvolvedor em:

1. Selecionar somente os dados de países das Américas
2. Eliminar países com dados faltantes
3. Transformar os dados de excel em um csv com as colunas: Continente, País, Mês, Numero de Visitantes, Lat, Long e Sigla. Essa transformação incluiu inclusive o levantamento das latitudes e longitudes de cada país, bem como a sigla internacional de 3 letras utilizada.

Ainda, o Chat-GPT foi utilizado para criar a imagem do Rio de Janeiro constante da Home do aplicativo, bem como gerar as docstrings das funções.

Caso queira testar o aplicativo, o arquivo turistas_2019 constante da pasta 02_processed pode ser utilizado.

Por fim, caso deseje verificar o layout do aplicativo antes de executá-lo, uma versão de cada página consta na pasta layout.