import pandas as pd
import plotly.express as px
import streamlit as st
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )
print(df)
