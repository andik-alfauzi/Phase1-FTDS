import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title = 'Phase 1 - Milestone 2',
    layout = 'wide',
    initial_sidebar_state='expanded'
)

def run():
    # Buat title
    st.title('Insurance Charges Prediction')

    # Buat sub header
    st.subheader('EDA untuk Analisa Dataset Insurance')

    # Menambahkan gambar
    # Define function gambar
    image = Image.open('Data_Explain.png')
    # Function implementation
    st.image(image, caption='Data_Explain')

    # Menambahkan deskripsi
    st.write('Page made by *Andik Al Fauzi*')

    # Membuat garus lurus
    st.markdown('----')

    # Explaination of model deployment
    '''
    Pada Page kali ini, penulis akan melakukan explorasi sederhana.
    Dataset yang dipakai adalah dataset Insurance yang diambil dari Kaggle
    Project ini adalah instruksi dari Assignment di Milestone 2
    '''

    # Show dataframe
    data = pd.read_csv('https://raw.githubusercontent.com/andik-alfauzi/Phase1-FTDS/main/Milestone/p1-ftds018-rmt-m2-andik-alfauzi/insurance.csv')
    st.dataframe(data)

    # Membuat Histogram Sex
    st.write('### Histogram of Sex')
    fig = plt.figure(figsize=(15, 6))
    sns.histplot(data['sex'], bins=50, kde=True)
    st.pyplot(fig)

    # Plot bmi by smoker
    fig = go.Figure(data=[go.Scatter3d(
        x = data['age'],
        y = data['children'],
        z = data['charges'],
        mode='markers',
        marker=dict(
            size = 10,
            color = data['age'],
            colorscale = 'Viridis',
            opacity = 0.8
        ),
        text = data['charges'],
        hoverinfo='text'
    )])

    fig.update_layout(
        scene = dict(
            xaxis = dict(title='age'),
            yaxis = dict(title='children'),
            zaxis = dict(title='charges')
        ),
        title = 'BMI of Smoker'
    )

    st.plotly_chart(fig)

    # Membuat Histgram base on user input
    st.write('#### Histogram base on user input')
    pilihan = st.selectbox('Pilih Column : ', ('age', 'sex', 'bmi', 'region'))
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(data[pilihan], bins=30, kde=True)
    st.pyplot(fig)

if __name__ == '__main__':
    run()