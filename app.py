import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

st.header('Data Visualization')

histogram = st.checkbox('\'Model Year\' vs \'Condition\' Histogram')
chart = st.checkbox('Chart')

if histogram:
    st.subheader('Histogram')
    fig = px.histogram(data, x='model_year',color='condition')
    st.plotly_chart(fig, use_container_width=True)

if chart:
    st.subheader('Chart')
