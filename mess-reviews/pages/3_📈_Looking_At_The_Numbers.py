import streamlit as st
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
            Before we dive into the details of specific comparisons, let's take a step back and look at the bigger picture. In this section, we'll explore the general statistics and time series trends that shape our mess hall experiences.
            
            *(Remember we converted the ratings into percentages!)*""",unsafe_allow_html=True)
st.code("mess.describe(include=[float])")
mess.date = pd.to_datetime(mess.date)
mess = mess.astype({"mess": 'category', "day": 'category', "meal": 'category'})
st.dataframe(mess.describe(include=[float,int]), use_container_width=True)

st.markdown("""
            Perhaps unsurprisingly, the overall stats don't look that good. 
            
            - <p>The median for score is ~2.27 stars</p>
            - <p>Around a third of the people give an 'okay' rating (3 stars)</p>
            - <p>The 'excellent' or 5 star option seems to be inflicted with outliers, because the mean is quite inflated as compared to the median (almost 4 times!)</p>
            - <p>On the contrary, there is one poll where 100% of the people gave a 1 star</p>
            - <p>Out of a 1000+ people present in the group, less than 100 people bother voting</p>
            
            """
            ,unsafe_allow_html=True)

st.markdown("""
            ---
            # Time Series
            While I have put the option to see the time series of any stat you wish, I will primarily analyze the number of votes per poll with respect to time.""",unsafe_allow_html=True)
with st.expander(label="Select an option to see its variation (in %) over time", expanded=True):

    feature = st.selectbox(
        label=" ", options=['votes','score','excellent', 'good', 'okay', 'poor'])
    fig = px.line(mess, x='date', y=f'{feature.lower()}')
    fig.update_xaxes(
        dtick="M1",
        tickformat="%b",
        rangeslider_visible=True,)
    fig.update_traces(line_color='#57A6A1')
    fig.update_layout(hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)   

st.markdown("""
            - <p>The number of votes/poll starts off high, then sharply decreases and the poll frequency is also very low (the 2023 mess group was not that active)</p>
            - <p>A spike is observed when the even semester starts, and the polls are now being conducted much more frequently (the second group is created which consists of ALL the college students)</p>
            - <p>However, it gradually decreases as the semester goes on.</p>
            - <p>Another surge is seen in votes around April when the tender changes, as people are more eager to give feedback on the new menu.</p>
            - <p>There are no votes in the second half of December, due to end semester holidays</p>""",unsafe_allow_html=True)
st.info("""***Tasty Tidbits***\n\nThere are so many tiny nuances in this graph and each one can be attributed to some specific event like festivals, club activities, vacations and exam schedules... everything is interconnected!""",icon="🍒")
# color='mess',color_discrete_sequence=px.colors.qualitative.G10,
