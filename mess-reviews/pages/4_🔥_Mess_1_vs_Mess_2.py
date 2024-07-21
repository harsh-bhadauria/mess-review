import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(layout="wide",page_icon="🔥",page_title="Mess 1 vs Mess 2")

st.markdown("""
<style>
p {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🔥 Mess 1 vs Mess 2")

mess = pd.read_csv(Path(__file__).parents[1]/'data'/'mess_data_processed.csv')
mess.date = pd.to_datetime(mess.date)

st.markdown(
    """
     In this section, we'll compare the ratings of Mess 1 and Mess 2 to see which one reigns supreme! ~~(in the land of the blind, the one-eyed man is the king)~~ Did the tender change and introduction of non-veg items really make a huge impact on the overall quality of the food? Let's look at the data to find out.
    """,unsafe_allow_html=True)

st.title("Feature Comparison")
with st.expander(label="Select an option to compare its distribution", expanded=True):

    feature = st.selectbox(
        label="  ", options=['score', 'excellent', 'good', 'okay', 'poor','votes'])
    fig = px.histogram(
        mess, x=f"{feature}", 
        color="mess", 
        marginal="box", 
        hover_data=mess.columns,
        barmode="overlay",
        category_orders={"mess":[2,1]},
        color_discrete_map={2:"#00cecb",1:"palevioletred"})
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""
            After analyzing the distribution of various features, we are seeing a common pattern:
            
            - <p>The overall shape of distributions is roughly the same for both mess 1 and mess 2</p>
            - <p>There seems to be a higher number of polls conducted for mess 2 as compared to mess 1</p>
            - <p>Number of votes/poll are also higher for mess 2</p>
            - <p>Mess 1 does have slightly better stats overall, but that might just be because of lower number of polls and lower votes/poll</p>
            
            
            Let us quantify this difference by looking at the exact number of polls""",unsafe_allow_html=True)

mess_1_polls = mess.loc[mess.mess == 1,:].shape[0]
mess_2_polls = mess.loc[mess.mess == 2,:].shape[0]


st.code("""mess_1_polls = mess.loc[mess.mess == 1,:].shape[0]
mess_2_polls = mess.loc[mess.mess == 2,:].shape[0]
mess_1_polls,mess_2_polls""")
st.write(mess_1_polls,mess_2_polls)

st.info("""***Tasty Tidbits***\n\nRemember how the score distribution was positively skewed? That means if we randomly choose a point in our data, it is more likely to have a low score. Assuming any future polls will follow the same distibution, if you conduct a bunch more polls, the score is more likely to *decrease*. This is possibly why Mess 1 has a higher score- *it has lesser number of polls*.""",icon="🍒")

st.markdown("""
            ---
            # Tender Changes
            From April 2024, a new tender was issued for the central mess and various stationary and grocery shops on the campus. Most importantly, the whole mess menu changes, all the mess staff changes & non-veg items were now on the menu, being served in mess 2 ONLY (Previously, both mess had the same menu but served on alternate days). Will this drastic change have drastic consequences?
            """,unsafe_allow_html=True)

mess['new_tender'] = (mess.date) < np.datetime64("2024-04-01")
with st.expander(label="Select an option to compare its distribution", expanded=True):
    feature = st.selectbox(
        label=" ", options=['excellent', 'good', 'okay', 'poor','score','votes'])
    
    fig = px.histogram(mess,x="mess",
                       y=f"{feature}",
                       color="new_tender",
                       barmode="group",
                       histfunc='avg',
                       color_discrete_sequence={False:"green",True:"red"},
                       hover_data=[mess.mess])
    st.plotly_chart(fig, use_container_width=True)

st.markdown("At first glance it seems promising, as the number of 5 star ratings did increase (not so much for mess 2 as one might expect). But once you look at the other categories and finally get to the score... its essentitally the same. Even after poll frequency skyrocketing after the new tender, even after the introduction on non-veg items... nothing changed.")

st.markdown("""
            ---
            # Verdict
            After taking a look at the data, we can see that there's really not much difference in the score distributions. The quality of the food is essentially the same in both Mess 1 vs Mess 2. The tender changes did not have much impact on the ratings either.
            
            However, it is clear that more number of polls were conducted for Mess 2, leading to more accurate score ratings. The number of votes/poll also increased by about 10% for mess 2 (and *decreased* by about 12% for mess 1), so it seems like ***Mess 2 is in a better state now as compared to Mess 1***.
            """)