import streamlit as st
import plotly
import plotly.express as px
import pandas as pd
import json

def app():
    st.empty()
    page = st.container()

    page.title("Fees and Average Deposit and Withdrawel Sizes. ")

    query_id = "207f12b8-1ff4-45d1-ade6-4669914ff410"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
    )  

#-------------------------------------------------------
    
    page.markdown("""
    ### AAVE 29 SER
    """)

    df = px.line(
        df, #this is the dataframe you are trying to plot
        x = "DAYZD",
        y = ["FEED","FEEB"],
        #color = columns,
        title = "AVG FEEZ by action: FEED is avg fee for deposit and FEEB is avg fee for borrow",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = False
    )
    

    page.plotly_chart(df)
    query_id = "207f12b8-1ff4-45d1-ade6-4669914ff410"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAYZD",
        y = ["FEED","FEEB"],
        #color = columns,
        title = "AVG FEEZ by action: FEED is avg fee for deposit and FEEB is avg fee for borrow",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = False
    )
    

    page.plotly_chart(df)


    query_id = "207f12b8-1ff4-45d1-ade6-4669914ff410"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.line(
        df, #this is the dataframe you are trying to plot
        x = "DAYZD",
        y = ["AVG(SUPPLIED_USD)","AVG(BORROWED_USD)"],
        #color = columns,
        title = "AVG USD in/out by action",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = False
    )
    page.plotly_chart(df)
    query_id = "207f12b8-1ff4-45d1-ade6-4669914ff410"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAYZD",
        y = ["AVG(SUPPLIED_USD)","AVG(BORROWED_USD)"],
        #color = columns,
        title = "AVG USD in/out by action",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = False
    )
    page.plotly_chart(df)

    query_id = "207f12b8-1ff4-45d1-ade6-4669914ff410"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.line(
        df, #this is the dataframe you are trying to plot
        x = "DAYZD",
        y = ["DRATIO","BRATIO"],
        #color = columns,
        title = "Special Ratio. Ratio of AMOUNT USD to Fee in USD, categorized by D(deposit) and B(Borrow)",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = False
    )
    page.plotly_chart(df)
    query_id = "207f12b8-1ff4-45d1-ade6-4669914ff410"
    df = pd.read_json(f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
    df = px.scatter(
        df, #this is the dataframe you are trying to plot
        x = "DAYZD",
        y = ["DRATIO","BRATIO"],
        #color = columns,
        title = "Special Ratio. Ratio of AMOUNT USD to Fee in USD, categorized by D(deposit) and B(Borrow)",
        orientation = "v",
        template = "plotly_white",
        width = 1000,
        height = 600,
        log_y = False
    )
    page.plotly_chart(df)



# DAYZD	AVG(SUPPLIED_USD)	FEED	DRATIO
# DAYZB	AVG(BORROWED_USD)	FEEB	BRATIO
    