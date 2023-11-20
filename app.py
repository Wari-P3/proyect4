import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

st.header('Data Visualization')

histogram = st.checkbox('\'Model Year\' vs \'Condition\' Histogram')
scatter_plot = st.checkbox('\'Odometer\' vs \'Price\' Scatter Plot')

if histogram:
    st.subheader('Histogram')
    fig = px.histogram(data, x='model_year',color='condition')
    st.plotly_chart(fig, use_container_width=True)

if scatter_plot:
    st.subheader('Scatter Plot')
    fig = px.scatter(data, x='odometer',y='price')
    st.plotly_chart(fig, use_container_width=True)
