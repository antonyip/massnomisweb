import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

def app():

    page = st.container()
    page.title("Eth Fees")
    page.text ("https://app.flipsidecrypto.com/velocity/queries/11edbedf-d84e-493d-b605-827298e317e2")



    eth_fees_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/11edbedf-d84e-493d-b605-827298e317e2/data/latest')

    t_f = False
    

#-------------------------------------------------------
    
    page.markdown("""
    ### Ethereum Fees and Transactions - Base Table
    """)

    page.dataframe(eth_fees_flipside_df)

    page.markdown("""
    """)
    




    eth_fees_graph = px.line(
        eth_fees_flipside_df, #this is the dataframe you are trying to plot
        x = "ETH_DAY",
        y = "TRANSACTION_COUNT",
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    page.plotly_chart(eth_fees_graph)

    

    eth_fees_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/11edbedf-d84e-493d-b605-827298e317e2/data/latest')
    eth_fees_graph = px.line(
        eth_fees_flipside_df, #this is the dataframe you are trying to plot
        x = "ETH_DAY",
        y = ["EFEES_USDAVG","EFEES_USDMED"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    page.plotly_chart(eth_fees_graph)


    eth_fees_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/11edbedf-d84e-493d-b605-827298e317e2/data/latest')
    eth_fees_graph = px.line(
        eth_fees_flipside_df, #this is the dataframe you are trying to plot
        x = "ETH_DAY",
        y = ["EFEES_USD"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    page.plotly_chart(eth_fees_graph)


    eth_fees_flipside_df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/11edbedf-d84e-493d-b605-827298e317e2/data/latest')
    eth_fees_graph = px.line(
        eth_fees_flipside_df, #this is the dataframe you are trying to plot
        x = "ETH_DAY",
        y = ["EZ1","EFEES_USDSTD","EZN1"],
        #color = columns,
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = t_f
    )
    page.plotly_chart(eth_fees_graph)
    # ------------------------------------------------

#   eth_day
#    transaction_count
# efees_usd
#  efees_usdavg
# efees_usdmed
#   efees_usdstd
# eZ1
#   eZn1