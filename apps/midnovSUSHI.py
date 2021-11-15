import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

def app():

    #st.set_page_config(layout="wide")
   



    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/204a4d8f-b1eb-4149-aefe-4d42c0da8e62/data/latest')

    t_f = False
    st.sidebar.write("Choose y-axis scale")
    check = st.sidebar.checkbox("Linear/Log")
    if check: 
        t_f = True
    

#-------------------------------------------------------
 

    




    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAYZ",
        y = "FROMM",
        color = "PLATFORM",
        orientation = "v",
        title = "1. Active Weekly Users",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)


# MONTH	UNI_VS_SUSHI	USD_MONTH_SUM	MONTH_AVERAGE_USD
    df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/81b05fe3-5951-4c4c-91ae-b4a8fa20e5b8/data/latest')
    df = px.bar(
        df, #this is the dataframe you are trying to plot
        x = "MONTH",
        y = ["USD_MONTH_SUM","MONTH_AVERAGE_USD"],
        color = "UNI_VS_SUSHI",
        orientation = "v",
        title = "Monthly Swap Volume",      
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    st.plotly_chart(df)    
# # DHOUR	COUNT(POOL_NAME)	POOL_NAME