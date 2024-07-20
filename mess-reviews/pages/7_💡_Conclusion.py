import streamlit as st
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from pathlib import Path

st.set_page_config(layout="wide",page_icon="💡",page_title="Conclusion")

st.markdown("""
<style>
p {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

mess = pd.read_csv(Path(__file__).parents[1]/'data'/'mess_data_processed.csv')

st.title("💡 Conclusion")

st.markdown("""
            This mess review analysis has given a detailed look into the dining experiences within our college. We've broken down how the day of the week and meal times influence our ratings, revealing that certain days and meals consistently fare better or worse. We also compared Mess 1 against Mess 2, in the hopes to see if the tender changes lead to any changes. Further, we looked into outliers to shed light on those exceptional days when ratings soared or plummeted, offering insights about what works and what doesn't in our mess.
            
            The journey to a better mess experience is a collaborative effort. It involves feedback from students, adjustments by the mess staff, and an active mess committee. 
            Although the current ratings may not uphold our high standards, they do provide a baseline for further improvement.
            
            This project was meant for identifying the areas where we're lacking and then taking steps to counter those problems. By understanding patterns, we can make informed decisions to enhance our overall mess experience. I hope that the insights gained from this analysis are helpful, even if just a little bit.
            
            The new tender may not have had the drastic impact we thought it would, but it was a step in the right direction. The increased poll frequency is a step in the right direction. Perhaps this project is a step in the right direction. And if there's anything that I've learned from Gradient Boost, its that taking tiny steps in the right direction will eventually lead you to your desired destination.
            
            """,unsafe_allow_html=True)

# This review analysis of the mess has been useful in taking a detailed look into the dining experiences that are served within our college. We broke down how the day of the week and meal times influenced our rating, revealing some strong trends for days/meal times that consistently fared worse or better. We have also compared Mess 1 against Mess 2 in the hope of seeing whether the tender changes will bring about any changes. We have also looked at outliers to shed some light on those exceptional days when ratings were very high or low, in search of clues about what works and does not work with our mess.
# At least the insights learned from this analysis are useful. This project is not intended to point out what's wrong; it's to work out how to fix it. Maybe zeroing in on trouble spots and time out to celebrate things we're doing right could go hand-in-hand. These patterns can help us make decisions that will have an improved overall mess experience.
# The better mess experience is a joint journey. It consists of student feedback, mess staff adjustments, and an active mess committee.
# Although the current ratings do not picture any of the high standards we believe we should be rated, they still provide us with a baseline for further improvement.

# The new tender was not quite as drastically directive as we would have hoped, but it was in the right direction.            Increasing the poll frequency at least sounds like it's a step in the right direction. Perhaps this project is a step in the right direction. And if there's anything I've taken away from Gradient Boost, it's that taking small steps in the right direction will get you there. 