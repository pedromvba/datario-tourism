import streamlit as st
import os 

st.set_page_config(
    page_title="Main Page",
    page_icon="👋",
)



# cleaning any previous uploaded data
uploaded_path = './data/03_uploaded/uploaded_file.csv'

# initializing session state to track file_state parameter shared between app.py and Introdução.py
if 'file_state' not in st.session_state:
    st.session_state['file_state'] = 0

# checking if the file exists
if (os.path.isfile(uploaded_path)) and (st.session_state['file_state'] == 0): # if file state == 1, then a new file was uploaded
    os.remove(uploaded_path)
    st.write('Removido')

st.header('Bem Vindo ao TouristInsight RJ 🏖️')
st.image('./images/riodejaneiro.jpg')

st.write('''
         O objetivo do dashboard é facilitar análises com relação a nacionalidade de turistas que chegaram no Rio de Janeiro,
         em determinado ano, por via aérea. E a partir dessa análise permitir que sejam obtidos insights sobre os países dos quais
         se originam os turistas, de forma a identificar públicos alvo de campanhas publicitárias.

         Para a correta utilização do aplicativo, favor iniciar o uso pela abra Introdução na qual será possível realizar o upload dos dados.
         Após o upload, a aba Explorar Dados poderá ser utilizada para obter os insights a partir da aplicação de filtros e
         visualização de informações gráficas sobre os dados.
         ''')

# Q6 e Q8

# creating ther session state
if 'backgroud_state' not in st.session_state:
    st.session_state['backgroud_state'] = '#FFFFFF'

#initializing with white and picking a new color
background_color = st.color_picker(
    label='Caso deseje alterar a cor do aplicativo para um maior conforto visual, escolha e aplique uma nova cor abaixo:',
    value=st.session_state['backgroud_state'])

#updating session state
st.session_state['backgroud_state'] = background_color

# applying the backgroud color
st.markdown(
    f'''
    <style>
    [data-testid="stApp"] {{
        background-color: {st.session_state['backgroud_state']}
    }}
    </style>
    ''',
    unsafe_allow_html=True)




