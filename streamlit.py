import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
import time

st.set_page_config(
    page_title="TSA Data",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state = "collapsed",
)

st.title("El Puto AMO de RONGOA")

#col1, col2, col3 = st.beta_columns(3)
#with col1:
#   st.header("Un Gato")
#   st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)
#with col2:
#   st.header("A dog")
#   st.image("https://static.streamlit.io/examples/dog.jpg", use_column_width=True)
#with col3:
#   st.header("An owl")
#   st.image("https://static.streamlit.io/examples/owl.jpg", use_column_width=True)

url = "https://api-dolar-argentina.herokuapp.com/api/dolarblue"
payload = {}
files = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

#st.write(response.json())

data_string = json.dumps(response.json())
decoded = json.loads(data_string)
compra=float(decoded["compra"])
venta=float(decoded["venta"])


if st.checkbox("Blue Compra", help="Mostrar valor Compra Dolar Blue"):
    colV, colC = st.columns(2)
    with colV:
        st.header("Venta")
        st.write(venta)
    with colC:
        st.header("Compra")
        st.write("Compra", compra)

st.button("bla")
st.warning("Guarda!")
st.info('Aca la sigo cagando con la hora de irme a dormir como un nerd')

#my_bar = st.progress(0)
#for percent_complete in range(100):
#    time.sleep(0.1)
#    my_bar.progress(percent_complete + 1)

#left_column, right_column = st.beta_columns(2)
#pressed = left_column.button('Press me?')
#if pressed:
#    right_column.write("Woohoo!")


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(pd.DataFrame({
    'Columna 1': ["A", "B", "C", "D"],
    'Columna 2': [10, 20, 30, 40]
}))

if st.checkbox("Mostrar Mapa"):
    map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
    st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

############ Sidebar ###############
st.sidebar.write("Menu")

dif = st.sidebar.slider("Dif",value=10)
st.sidebar.write(dif)

st.sidebar.selectbox("How would you like to be contacted?",("Email", "Home phone", "Mobile phone"))

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option
###################################
