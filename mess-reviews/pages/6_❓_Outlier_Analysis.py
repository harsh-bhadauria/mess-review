import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from pathlib import Path
from PIL import Image

st.set_page_config(layout="wide",page_icon="❓",page_title="Outlier Analysis")

st.markdown("""
<style>
p {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

mess = pd.read_csv(Path(__file__).parents[1]/'data'/'mess_data_processed.csv')

st.title("❓ Outlier Analysis")
st.markdown("""
            In this section, we explore the intriguing outliers in our data—the days when ratings either skyrocket or take a plunge into the abyss. What causes these unexpected highs and lows? Is it a special festive dish that reminds you of home, or were the rotis burned to a crisp?
            
            Let's start by looking at specific days where the ratings were highest and try to guess why that might be
            """,unsafe_allow_html=True)
st.code("""mess.sort_values("score",ascending=False).loc[:,["date","score"]].head(10)""")

st.dataframe(mess.sort_values("score",ascending=False).loc[:,["date","score","mess","meal","day"]].head(10),use_container_width=True)

st.markdown("""
            Two dates stand out in particlar: 28-01-2024 and 09-04-2024
            - <p><b><em>28th January</em></b>: Pongalo Pongalo! This was the day that Pongal festivities took place in our college. The actual dates for Pongal were 15th January - 18th January, but due to a power shortage that lasted more than it should've, the celebrations were delayed. Anyhow, on this date there was a special lunch organized by the Telugu community and it is no surprise the score is 4.9, highest it has ever been. </p>
            - <p><b><em>9th April</em></b>: Gudi Padwa and Ugadi. This date marked the beginning of a new year in the Hindu calendar celebrated in many states of India by different names. On this date too there was a special breakfast as well as a special lunch, organised by the Marathi and the Telugu communities respectively. The score is 4.8, and rightfully so.</p>
            
            """,unsafe_allow_html=True)
st.markdown("Well well well... that was a pleasant trip down memory lane. Now let's look at the opposite side of the spectrum shall we?")
st.code("""mess.sort_values("score",ascending=False).loc[:,["date","score"]].head(10)""")

st.dataframe(mess.sort_values("score").loc[:,["date","score","mess","meal"]].head(10),use_container_width=True)

st.markdown("""
            Although there's no explicit outlier here, there is still one thing which I was baffled to see. You might've guessed it, there is an entry which has a score of EXACTLY 1.
            
            ***The lunch of 10th April, 2024***
            
            What on earth could possibly have been so bad in taste, that the entirety of the college set aside their differences and came together to give it the worst rating possible? There is not a single vote in any of the other categories, not a single one. And its not like there's only a handful votes on that poll, there's 85. Take a look for yourself-
            """)
image_path = Path(__file__).parents[1] / 'images' / '10th_april.png'
food_bg = Image.open(image_path)
st.image(food_bg,use_column_width="auto")

st.markdown("""Although I personally have not eaten this legendary rasam (I was in Mess 1), I would like to ask someone what it was like.""")