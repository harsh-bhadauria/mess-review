import streamlit as st
from st_pages import add_page_title
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

st.set_page_config(layout="wide",page_icon="🔥",page_title="Mess 1 vs Mess 2")

st.markdown("""
<style>
p {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🔥 Mess 1 vs Mess 2")

mess = pd.read_csv("data/mess_data_processed.csv")
mess.date = pd.to_datetime(mess.date)

st.markdown(
    "Does it really make a difference if you're in mess 1 or mess2? Let's see what the data says!")

st.title("Feature Comparison")
with st.expander(label="Select an option to see its distribution", expanded=True):

    feature = st.selectbox(
        label="", options=['score', 'excellent', 'good', 'okay', 'poor','votes'])
    fig = px.histogram(
        mess, x=f"{feature}", 
        color="mess", 
        marginal="box", 
        hover_data=mess.columns,
        barmode="overlay",
        category_orders={"mess":[1,2]},
        color_discrete_map={1:"#b84b77",2:"#63e0d8"})
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""
            After analyzing the distribution of various features, we are seeing a common pattern:
            
            - <p>The overall shape of distributions is roughly the same for both mess 1 and mess 2</p>
            - <p>There seems to be a higher number of polls conducted for mess 2 as compared to mess 1</p>
            - <p>Number of votes per poll are also higher for mess 2</p>
            - <p>Mess 1 does have slightly better stats overall, but that might just be because of lower number of polls and lower votes per poll</p>
            
            
            Let us quantify this difference by looking at the exact number of polls""",unsafe_allow_html=True)

mess_1_polls = mess.loc[mess.mess == 1,:].shape[0]
mess_2_polls = mess.loc[mess.mess == 2,:].shape[0]

st.code("""mess_1_polls = mess.loc[mess.mess == 1,:].shape[0]
mess_2_polls = mess.loc[mess.mess == 2,:].shape[0]
mess_1_polls,mess_2_polls""")
st.write(mess_1_polls,mess_2_polls)

st.header("Tender Changes")
st.markdown("""From April 2024, a new tender was issued for the central mess and various stationary and grocery shops on the campus. Most importantly, non-veg items were now on the menu, being served in mess 2 ONLY (Previously, both mess had the same menu but served on alternate days). How did this affect the ratings?""",unsafe_allow_html=True)

mess['new_tender'] = (mess.date) < np.datetime64("2024-04-01")
with st.expander(label="Select an option to see its variation (in %) over time", expanded=True):
    feature = st.selectbox(
        label=" ", options=['excellent', 'good', 'okay', 'poor','score','votes'])
    
    fig = px.histogram(mess,x="mess",y=f"{feature}",color="new_tender",barmode="group",histfunc='avg')
    st.plotly_chart(fig, use_container_width=True)

st.markdown("At first glance it seems promising, as the number of 5 star ratings did increase (not so much for mess 2 as one might expect). But once you look at the other categories and finally get to the score... its essentitally the same. Even after poll frequency skyrocketing after the new tender, even after the introduction on non-veg items... nothing changed.")