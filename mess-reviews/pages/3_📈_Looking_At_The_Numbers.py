import streamlit as st
from st_pages import add_page_title
import numpy as np
import pandas as pd
import plotly.express as px
from pathlib import Path


st.set_page_config(layout="wide",page_icon="📈",page_title="Looking at the Numbers")

st.markdown("""
<style>
p {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.title("📈 Looking at the Numbers")

mess = pd.read_csv(Path(__file__).parents[1]/'data'/'mess_data_processed.csv')

st.markdown("""
            Before we dive into the delicious details of specific comparisons, let's take a step back and look at the bigger picture. In this section, we'll explore the general statistics and time series trends that shape our mess hall experiences. Think of it as the appetizer before the main course—an overview that sets the stage for the culinary insights to come.
            
            *(Remember we converted the ratings into percentages!)*""",unsafe_allow_html=True)
st.code("mess.describe(include=[float])")
mess.date = pd.to_datetime(mess.date)
mess = mess.astype({"mess": 'category', "day": 'category', "meal": 'category'})
st.dataframe(mess.describe(include=[float,int]), use_container_width=True)

st.markdown("""
            Perhaps unsurprisingly, the overall stats don't look that good. 
            - The median for score is ~2.27, which is basically 2 stars or 'below average'
            - Around a third of the people give an 'okay' rating (3 stars)
            - The 'excellent' or 5 star option seems to be inflicted with outliers, because the mean is quite inflated as compared to the median (almost 4 times!)
            - On the contrary, there is one poll where 100% of the people gave a 1 star
            - Out of a 1000+ people present in the group, only ~100 people bother voting"""
            ,unsafe_allow_html=True)

text = st.markdown("# Time Series")
with st.expander(label="Select an option to see its variation (in %) over time", expanded=True):

    feature = st.selectbox(
        label="", options=['votes','score','excellent', 'good', 'okay', 'poor'])
    fig = px.line(mess, x='date', y=f'{feature.lower()}', hover_data=['poor'],)
    fig.update_xaxes(
        dtick="M1",
        tickformat="%b",
        rangeslider_visible=True)
    fig.update_yaxes(title=f"% of {feature} ratings")
    st.plotly_chart(fig, use_container_width=True)   

st.markdown("""
            The number of votes per poll stat in particular has an interesting story to tell:
            - It starts off high, then sharply decreases and the poll frequency is also very low (the 2023 mess group was not that active)
            - A spike is observed when the even semester starts, and the polls are now being conducted much more frequently (the group now consists of ALL the college students)
            - However, it gradually decreases as the semester goes on.
            - Another surge is seen in votes when the tender changes, as people are more eager to give feedback on the new menu.
            - There are many tiny nuances that can be attributed to events like festivals, club activities and exam schedules, everything is interconnected!""",unsafe_allow_html=True)
# color='mess',color_discrete_sequence=px.colors.qualitative.G10,
