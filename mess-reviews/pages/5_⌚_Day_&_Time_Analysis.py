import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import datetime

st.set_page_config(layout="wide",page_icon="⌚",page_title="Day & Time Analysis")

st.markdown("""
<style>
p {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

mess = pd.read_csv(Path(__file__).parents[1]/'data'/'mess_data_processed.csv')
mess.date = pd.to_datetime(mess.date)

st.title("⌚ Day & Time Analysis")

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
    


with st.expander(label="Select an option to see its variation as the day and meal changes", expanded=True):
    feature = st.selectbox(
        label="  ", options=['score','excellent', 'good', 'okay', 'poor','votes'])
    
    fig = px.histogram(
        mess,x="day",
        y=f"{feature}",
        color='meal',
        category_orders=dict(day=["Monday", "Tuesday", "Wednesday", "Thursday","Friday","Saturday","Sunday"],meal=["breakfast","lunch","dinner"]),
        barmode="group",
        hover_data=mess.columns,
        histfunc='avg',
        labels={'day':""},
        color_discrete_map={'breakfast':"#1b9aaa","lunch":"#ffbc42","dinner":"#d81159"})
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""
            - <p>The highest score is taken by <em>*insert drumroll*</em> Sunday breakfasts! (Can you blame em? Those aloo parathas and dosas were so good. Well... relatively at least)</p>
            - <p>Lunches have a consistently high score all across the board- even the worst lunch has ~1.5x the score of the worst dinner</p>
            - <p>On the other hand, dinners have the lowest ratings overall. In fact, the lowest score is prominently taken by Saturday dinners, having the lowest %good and highest %poor ratings (people *really* didn't like those chilli potatoes)</p>
            - <p>Tuesday and Sunday seem to have an unusually high amount of 5 star ratings, suggesting the presence of outliers (as we will see in the next section, thats absolutely correct!)</p>
            - <p>Wednesday sees the highest number of votes/poll for all three meals combined</p>
            - <p>Dinners get the highest number of votes per poll (people dont wake up early enough for breakfast, and there's usually classes before and/or after lunch)</p>
            
            """,unsafe_allow_html=True)

st.info("""***Tasty Tidbits***\n\nWhen looking at a graph, it is very important to look at the scale of the axes. Here the terms 'best' and 'good' are relative. In fact, no meal on any day reaches even the 3 star mark.""",icon="🍒")

st.markdown("""
            ---
            # Daily Graph
            I'm including a daily plot which shows a quick summary of the stats of any specified date. Although it is not feasible to analyze every single day, this can be used to investigate outliers and I think its more of a QoL feature.
            """)

with st.expander(label="Please select a date",expanded=True):
    date = st.date_input(" ",
                         min_value=datetime.date(2023,9,21),
                         max_value=datetime.date(2024,4,11),
                         format="DD-MM-YYYY",
                         value=None)
    
    labels = ['Excellent','Good','Okay','Poor']
    date_ratings = mess.loc[mess.date == np.datetime64(date),["excellent","good","okay","poor","score","votes"]]
    if(date_ratings.empty == False):
        
        data = {
            "Average Score":[round(date_ratings.score.mean(),2)],
            "No. of Polls":[date_ratings.shape[0]],
            "Average Votes/Poll": [round(date_ratings.votes.sum()/date_ratings.shape[0])]
            }
        
        st.dataframe(pd.DataFrame(data),use_container_width=True,hide_index=True)
        values = date_ratings.drop(["score","votes"],axis=1).mean()
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        fig.update_traces(hoverinfo='label+percent',marker=dict(colors = ['#00cecb','#7fb800','#ffbc42','d81159']))
        st.plotly_chart(fig, use_container_width=True)
        #st.write(np.datetime64(date))
        
        st.dataframe(mess.loc[mess.date == np.datetime64(date),:].drop(["date","day"],axis=1),use_container_width=True)
        
    else: st.code("There were no polls conducted on this date :(")

