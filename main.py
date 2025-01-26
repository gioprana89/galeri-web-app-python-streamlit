import streamlit as st 

st.set_page_config(layout="wide")

import pandas as pd

import numpy as np

import plotly.graph_objects as go

import plotly.express as px







st.write('''<br><br><br><center><font color = "#0000ff" size = 7>GALERI APLIKASI PYTHON-STREAMLIT</font></center>



             ''', unsafe_allow_html = True)




col1, col2, col3, col4, col5 = st.columns([3,3,3,3,3])

with col1:
    st.write("") 

with col2:
    st.write("") 

with col3:
    st.image("ugi3.jpg", width = 300)

with col4:
    st.write("")

with col5:
    st.write("")




st.markdown(
    """<center><a href="https://galeri-web-app-python-2025.streamlit.app/" target = "_blank">Galeri Aplikasi Python-Streamlit</a> | <a href="https://statkomat.com/download_tulisan.php" target = "_blank">STATKOMAT</a> | <a href="https://www.youtube.com/@STATKOMAT" target = "_blank">Youtube</a> | <a href="https://share-your-shiny-app.id/" target = "_blank">Shiny</a></center><br><br>""",
    unsafe_allow_html=True)




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
    st.write("<h5 style='text-align: justify; color: blue;'><a href = 'https://galeri-python-app-tabel-5.streamlit.app/' target = '_blank'>Aplikasi Data Tabel-5 (Multiselect Widget)</a></h3>", unsafe_allow_html=True)
    st.image("tabel5.png")


with col31:
    st.write("<h5 style='text-align: justify; color: blue;'><a href = '' target = '_blank'>Aplikasi Data Tabel-6</a></h3>", unsafe_allow_html=True)



























st.write('''<br><br><br><center><font color = "#ff0090" size = 8>APLIKASI DATA LITERATUR</font></center>



             ''', unsafe_allow_html = True)






col21, col22, col23 = st.columns(3)

with col21:
    st.write("<h5 style='text-align: justify; color: blue;'><a href = 'https://aplikasi-plssem-datakeuangan-hargasaham-endogen.streamlit.app/' target = '_blank'>Kumpulan Artikel (Jurnal & Prosiding): Aplikasi Partial Least Squares Structural Equation Modeling (PLS-SEM) dengan Variabel Harga Saham sebagai Variabel Endogen</a></h3>", unsafe_allow_html=True)
    st.image("dataliteratur1.png")

with col22:
    st.write("")


with col23:
    st.write("")



