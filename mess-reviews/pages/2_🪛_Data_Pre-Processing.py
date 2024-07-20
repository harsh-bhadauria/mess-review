import streamlit as st
from st_pages import add_page_title, hide_pages
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from sklearn.preprocessing import RobustScaler
from pathlib import Path

st.set_page_config(layout="wide",page_icon="🪛",page_title="Data Pre-Processing")

st.markdown("""
<style>
p {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🪛 Data Pre-Processing")


mess = pd.read_csv(Path(__file__).parents[1]/'data'/'mess_data.csv')

st.markdown("""
            # Data types and Calculating score
            Because we will be doing date comparisons and plotting many many graphs, it is important that we first convert the object data type columns into their appropriate data type
            """, unsafe_allow_html=True)

st.code("""
        # Converting date to datetime and both mess and day to category
        import pandas as pd
        mess = pd.read_csv("data/mess_data.csv")
        mess.date = pd.to_datetime(mess.date)
        mess = mess.astype({"mess":'category',"day":'category',"meal":'category'})""")

mess.date = pd.to_datetime(mess.date)
mess = mess.astype({"mess":'category',"day":'category',"meal":'category'})

st.markdown("""
            Now we need a metric which condenses the poll results into a more digestible (ha, get it?)format. How about we add a star point rating system? We'll give each poll a rating out of five based on the ratings it received. More formally, we will add a 'score' feature, which will be a weighted average of other ratings. The weights are designated as follows:
            
            - <p>Excellent = 5 stars    :D</p>
            - <p>Good = 4 stars &ensp; :)</p>
            - <p>Okay = 3 stars &ensp; :|</p>
            - <p>Poor = 1 star &emsp; :(</p>
            
            """, unsafe_allow_html=True)

st.code("""
        total = mess['poor'] + mess['okay'] + mess['good'] + mess["excellent"]
        mess['score'] = (mess['poor']+3*mess['okay']+4*mess['good']+5*mess["excellent"])/(total)
        """)


total = mess['poor'] + mess['okay'] + mess['good'] + mess["excellent"]
mess['score'] = (mess['poor'] + 3*mess['okay'] + 4*mess['good']+ 5*mess["excellent"])/(total)
mess['votes'] = total

st.markdown("---\nNow if we take a look at this weighted average of ratings:")

fig = px.histogram(mess.score)

fig.update_layout(
    xaxis_title="score",
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)
st.info("""***Tasty Tidbits***\n\nWe can see the data is positively skewed. If we were to train an ML model on this data, we would have to apply some sort of transform (sqrt, log, etc.) However because its just for EDA purposes, we will preserve the original data.""",icon="💡")

st.markdown("Lets draw to a box plot to understand this score parameter better: ")
# st.markdown(
#     "As expected, the data is positively skewed. We shall apply a log transformation")
# st.code("score = np.log10(mess.score+0.3)")

# mess.score = np.log10(mess.score+0.3)

# fig = ff.create_distplot([mess.score], ['score'], bin_size=[0.05])

# fig.update_layout(
#     xaxis_title="log10(score+0.3)",
#     yaxis_title="count", showlegend=False
# )

# st.plotly_chart(fig, use_container_width=True)
# st.markdown("Now it roughly looks like a normal curve.")

fig = px.box(mess,x='score')
st.plotly_chart(fig, use_container_width=True)


st.markdown("It would make sense to express the rating as percentages instead of raw numbers, to make them independent of the total number of votes that day. Now instead of looking at how many people voted 'good', we want the _percentage_ of people that voted 'good'. We will add a separate column for the total number of votes on a poll, because that is indeed valuable information")
st.code("""
        total = mess['excellent']+mess['good']+mess['okay']+mess['poor']
        mess['votes'] = total
        
        mess['excellent'] *= 100/total
        mess['good'] *= 100/total
        mess['okay'] *= 100/total
        mess['poor'] *= 100/total
        
        """)


total = mess['excellent']+mess['good']+mess['okay']+mess['poor']
mess['excellent'] *= 100/total
mess['good'] *= 100/total
mess['okay'] *= 100/total
mess['poor'] *= 100/total

mess.to_csv(Path(__file__).parents[1]/'data'/'mess_data_processed.csv', index=False)


