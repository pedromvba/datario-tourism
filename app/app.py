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

st.write(os.path.isfile(uploaded_path))
st.write(st.session_state['file_state'])


st.header('Bem Vindo ao TouristInsight RJ')
st.image('./images/riodejaneiro.jpg')

st.session_state # testando
