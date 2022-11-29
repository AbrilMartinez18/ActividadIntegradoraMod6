#!/usr/bin/env python
# coding: utf-8



#Actividad Integradora
#Abril Martínez Salas A01734613


#IMPORTAR LIBRERIAS
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import numpy as np
import scipy.stats
from scipy.stats import norm
import altair as alt




df=pd.read_csv("Police_Department_Incident_Reports__2018_to_Present.csv")


st.set_page_config(page_title="Police Department Incident Reports, from 2018 until 2020",layout='wide',page_icon=':police_car:')
st.title("Police Department Incident Reports, from 2018 to 2020 :cop:")
st.markdown("Collaboration between the San Francisco Council and SFPD")



from PIL import Image
image = Image.open('sanfran.jpeg')
st.image(image)



menu=st.sidebar.selectbox('Search for Information',options=['Location of Incidents years: 2018-2020','Incidences Per Day by Year','Incidences per Police District','Report Type (Records from 2018 to 2020)','Follow Status of Cases'])




#MAPA DE SAN FRANCISCO
if menu == 'Location of Incidents years: 2018-2020':
    LatX = df['Latitude'].dropna(axis = 0, how = 'any')
    LongY = df['Longitude'].dropna(axis = 0, how = 'any')

    mapaCrim = pd.DataFrame()
    mapaCrim['lat'] = LatX
    mapaCrim['lon'] = LongY
    #desplegar mapa
    st.map(mapaCrim)




#DATAFRAMES POR ANIO DE INCIDENCIA
A18=df[df['Incident Year']==2018]

A19=df[df['Incident Year']==2019]

A20=df[df['Incident Year']==2020]




#A18['Incident Day of Week'].value_counts()

#A19['Incident Day of Week'].value_counts()

#A20['Incident Day of Week'].value_counts()


dias=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

#incidentes por día 2018
y2018=[21845,21730,22534,21798,23416,22234,20220]
#incidentes por día 2019
y2019=[21352,21302,22185,20839,22771,21020,19656]
#incidentes por día 2020
y2020=[10781,10754,11466,10830,11650,10906,10224]
# Multiline plot
if menu == 'Incidences Per Day by Year':
    # Multiline plot
    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(x=dias, y=y2018, name='2018', line=dict(color='#e056dd', width=4)))

    fig2.add_trace(go.Scatter(x=dias, y=y2019, name='2019', line=dict(color='#51a6dd', width=4)))

    fig2.add_trace(go.Scatter(x=dias, y=y2020, name='2020', line=dict(color='#93ce2a', width=4, dash='dot')))

    fig2.update_layout(title='Trend of Incidences per day of the week', xaxis_title='Day of Week', yaxis_title='Concurrence')

    st.plotly_chart(fig2)

    
#GRÁFICA 3
chart_data_bars=pd.DataFrame()
policeDistrict=['Central','Northern','Mission','Southern','Tenderloin','Bayview','Ingleside','Taraval','Richmond','Park','Out of SF']
if menu == 'Incidences per Police District':
    fig3 = px.bar(chart_data_bars,x =policeDistrict,y=df['Police District'].value_counts(),color=df['Police District'].unique(),
                 title='Amount of Crimes per Police District')
    st.plotly_chart(fig3)

    
#Type of Incident category in 2018
reportType2018=A18['Report Type Description'].value_counts()
reportType2019=A19['Report Type Description'].value_counts()
reportType2020=A20['Report Type Description'].value_counts()

if menu == 'Report Type (Records from 2018 to 2020)':
    
    st.header("Report Classification")
    st.text(" 1. Initial: The first report filed for the incident")
    st.text(" 2. Vehicle: A special incident report related to stolen and/or recovered vehicles")
    st.text(" 3. Coplogic: Filed online by an individual")
    st.text(" 4.If the report type contains SUPPLEMENT, it is an update of an existing case")
    fig4 = px.pie(reportType2018, values=reportType2018.values, names=reportType2018.index, title='Report Type 2018')
    fig5 = px.pie(reportType2019, values=reportType2019.values, names=reportType2019.index, title='Report Type 2019')
    fig6 = px.pie(reportType2020, values=reportType2020.values, names=reportType2020.index, title='Report Type 2020')
    st.plotly_chart(fig4)
    st.plotly_chart(fig5)
    st.plotly_chart(fig6)

status=df['Resolution'].value_counts()
status18=A18['Resolution'].value_counts()
status19=A19['Resolution'].value_counts()
status20=A20['Resolution'].value_counts()

if menu == 'Follow Status of Cases':
    st.header("Current Status of Cases:")
    
    result=st.button("Show all current Case Status")
    a2018=st.button("Status in 2018")
    a2019=st.button("Status in 2019")
    a2020=st.button("Status in 2020")
    
    if result:
        fig7 = go.Figure(data=[go.Pie(labels=status.index, values=status.values, hole=.5,marker_colors=px.colors.qualitative.Plotly)])
        st.plotly_chart(fig7)
    if a2018:
        fig8 = go.Figure(data=[go.Pie(labels=status18.index, values=status18.values, hole=.5, marker_colors=px.colors.qualitative.Pastel)])
        st.plotly_chart(fig8)
    if a2019:
        fig9 = go.Figure(data=[go.Pie(labels=status19.index, values=status19.values, hole=.5,marker_colors=px.colors.qualitative.Pastel)])
        st.plotly_chart(fig9)
    if a2020:
        fig10 = go.Figure(data=[go.Pie(labels=status20.index, values=status20.values, hole=.5,marker_colors=px.colors.qualitative.Pastel)])
        st.plotly_chart(fig10)
       
    

    
