import streamlit as st
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from pathlib import Path

st.set_page_config(layout="wide",page_icon="⌚",page_title="Mess-terpeice Timing")

st.markdown("""
<style>
p {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

mess = pd.read_csv(Path(__file__).parents[1]/'data'/'mess_data_processed.csv')

st.title("⌚ Mess-terpeice Timing")

st.markdown("""
            Ever wondered if those Monday morning blues are actually because of the mess breakfast? Or why Friday dinners always seem to taste a little better? In this section, we dive into the delicious details of how the day of the week and the meal time (breakfast, lunch, or dinner) play a role in deciding the mess food ratings.
            
            """,unsafe_allow_html=True)

# with st.expander(label="Select an option to see its variation (in %) over time", expanded=True):
#     feature = st.selectbox(
#         label=" ", options=['excellent', 'good', 'okay', 'poor','score','votes'])
    
#     fig = px.histogram(
#         mess,x="meal",
#         y=f"{feature}",
#         color='mess',
#         barmode="group",
#         histfunc='avg',
#         color_discrete_map={1:"#b84b77",2:"#63e0d8"})
#     st.plotly_chart(fig, use_container_width=True)
    


with st.expander(label="Select an option to see its variation (in %) over time", expanded=True):
    feature = st.selectbox(
        label="  ", options=['score','excellent', 'good', 'okay', 'poor','votes'])
    
    fig = px.histogram(
        mess,x="day",
        y=f"{feature}",
        color='meal',
        category_orders=dict(day=["Monday", "Tuesday", "Wednesday", "Thursday","Friday","Saturday","Sunday"],meal=["breakfast","lunch","dinner"]),
        barmode="group",
        hover_data=mess.columns,
        histfunc='avg',)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""
            - <p>The highest score is taken by <em>*insert drumroll*</em> Sunday breakfasts! (Can you blame em? Those aloo parathas and dosas were so good. Well... relatively at least)</p>
            - <p>Lunches have a consistently high score all across the board- even the worst lunch has ~1.5x the score of the worst dinner</p>
            - <p>On the other hand, dinners have the lowest ratings overall.</p>
            - <p>In fact, the lowest score is prominently taken by Saturday dinners, having the lowest %good and highest %poor ratings (people *really* didn't like those chilli potatoes)</p>
            - <p>Tuesday and Sunday seem to have an unusually high amount of 5 star ratings, suggesting the presence of outliers</p>
            - <p>Wednesday sees the highest number of votes per poll for all three meals combined</p>
            - <p>Dinners get the highest number of votes per poll (people dont wake up early enough for breakfast, and there's usually classes before and/or after lunch)</p>
            """,unsafe_allow_html=True)