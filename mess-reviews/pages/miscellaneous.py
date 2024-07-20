import streamlit as st
from st_pages import add_page_title, hide_pages
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from sklearn.preprocessing import RobustScaler

st.set_page_config(layout="wide")
add_page_title()

mess = pd.read_csv("data/mess_data.csv")

st.markdown("""
<style>
p {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
            # Data types and Calculating score
            First we convert the object data type columns into their appropriate data type
            """, unsafe_allow_html=True)