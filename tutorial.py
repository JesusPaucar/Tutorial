import streamlit as st
import pandas as pd
import gdown

# id = 1k7EF5NR584v4tVvXX0Zndkk3vvrQshdn
@st.experimental_memo
def download_data():
  #https://drive.google.com/uc?id=YOURFILEID
  url = "https://drive.google.com/uc?id=1k7EF5NR584v4tVvXX0Zndkk3vvrQshdn"
  output = 'data.csv'
  gdown.download(url,output,quiet = False)

download_data()
data = pd.read_csv('data.csv', sep = ';', nrows = 1000000, parse_dates = ['FECHA_CORTE','FECHA_RESULTADO'])
st.dataframe(data.head(20))
edades = data['EDAD']
st.line_chart(edades)
