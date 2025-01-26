import streamlit as st 

st.set_page_config(layout="wide")

import pandas as pd

import numpy as np

import plotly.graph_objects as go

import plotly.express as px







st.write('''<br><br><br><center><font color = "#0000ff" size = 7>GALERI APLIKASI PYTHON-STREAMLIT</font></center>



             ''', unsafe_allow_html = True)




st.image("ugi300.png")




st.write("<h5 style='text-align: justify; color: blue;'>Hadirnya website ini bertujuan untuk menampilkan berbagai aplikasi yang dirancang menggunakan <a href = 'https://streamlit.io/' target = '_blank'><font color = 'blue' style='background-color: #00ff00'>python-streamlit.</font></a> Kode program dapat didownload secara gratis.</h5>", unsafe_allow_html=True)





st.write('''<br><br><br><center><font color = "#ff0090" size = 8>APLIKASI SPREADSHEET</font></center>



             ''', unsafe_allow_html = True)







col1, col2, col3 = st.columns(3)

with col1:
    st.write("<h5 style='text-align: justify; color: blue;'><a href = 'https://galeri-python-app-tabel-1.streamlit.app/' target = '_blank'>Aplikasi Data Tabel-1</a></h3>", unsafe_allow_html=True)
    st.image("tabel1.png")

with col2:
    st.write("<h5 style='text-align: justify; color: blue;'><a href = 'https://galeri-python-app-tabel-2.streamlit.app/' target = '_blank'>Aplikasi Data Tabel-2 (Data Link)</a></h3>", unsafe_allow_html=True)
    st.image("tabel2.png")

with col3:
    st.write("<h5 style='text-align: justify; color: blue;'><a href = 'https://galeri-python-app-tabel-3.streamlit.app/' target = '_blank'>Aplikasi Data Tabel-3 (Multiselect Widget)</a></h3>", unsafe_allow_html=True)
    st.image("tabel3.png")





col11, col21, col31 = st.columns(3)

with col11:
    st.write("<h5 style='text-align: justify; color: blue;'><a href = 'https://galeri-python-app-tabel-4.streamlit.app/' target = '_blank'>Aplikasi Data Tabel-4 (Radio Button Widget)</a></h3>", unsafe_allow_html=True)
    st.image("tabel4.png")

with col21:
    st.write("<h5 style='text-align: justify; color: blue;'><a href = 'https://galeri-python-app-tabel-5.streamlit.app/' target = '_blank'>Aplikasi Data Tabel-4 (Radio Button Widget)</a></h3>", unsafe_allow_html=True)
    st.image("tabel5.png")



with col31:
    st.write("<h5 style='text-align: justify; color: blue;'><a href = '' target = '_blank'>Aplikasi Data Tabel-6</a></h3>", unsafe_allow_html=True)



























st.write('''<br><br><br><center><font color = "#ff0090" size = 8>APLIKASI DATA LITERATUR</font></center>



             ''', unsafe_allow_html = True)








