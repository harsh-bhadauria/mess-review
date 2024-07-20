import streamlit as st
from PIL import Image
from pathlib import Path

# shp(
#     [
#         pg("mess_review_analysis.py","Mess Review Analysis",icon="😋"),
#         pg("sidebar/data_collection.py",icon="📝"),
#         pg("sidebar/data_pre-processing.py",icon="🪛"),
#         pg("sidebar/looking_at_the_numbers.py",icon="📈"),
#         pg("sidebar/mess_1_vs_mess_2.py",icon="🔥"),
#         pg("sidebar/mess-terpiece_timing.py",icon="⌚"),
#         pg("sidebar/outlier_analysis.py",icon="❓"),
#         pg("sidebar/miscellaneous.py",icon="🤔"),
#     ]
# )
st.set_page_config(layout="wide",page_icon="😋",page_title="Mess Review Analysis")

#st.title("Mess-tery Solved: The Ultimate Poll Results")

# food_bg = Image.open(Path(__file__).parent/'food_final.png')
# #st.write(Path(__file__)/'mess_data.csv')
# st.image(food_bg)

image_path = Path(__file__).parent / 'images' / 'food_final.png'
food_bg = Image.open(image_path)
st.image(food_bg, caption='Mess Review Analysis Background')

st.markdown("""
<style>
p {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
            # Introduction
            <p>Welcome to the ultimate deep dive into our college dining experience— analyzing the mess reviews like never before! I’m conducting an in-depth mess review analysis using data collected by our very own college’s mess committee. From dissecting daily ratings to uncovering trends over time, this project aims to analyse the ups and downs of our mess dining experience. From basic stats and time series trends to head-to-head mess hall showdowns, there's something in here for everyone. Bon Appétit!</p>
            
            ---
            # Expectations
            <p> Some specific questions that I will try to analyse include (but are not limited to): </p>
            
            - <p>What is the overall quality of the mess food?</p>
            - <p>Which one out of Mess 1 and Mess 2 has a higher overall rating?</p>
            - <p>What is the frequency of the conducted polls?</p>
            - <p>How does the day and time affect ratings?</p>
            - <p>What was the impact of tender changes (if any)?</p>
            
            ---
            # Motivation
            <p>For this project, I wanted to focus on a dataset that's relevant to me and for our college community. Instead of analyzing a random dataset from the internet, I wanted to engage with something that reflects our daily experiences and offers actionable insights. After <del>a lot of</del> some brainstorming, I stumbled across polls that were conducted by the mess committee on WhatsApp (just goes to show that data is <em>everywhere</em> around you, you just have to look for it 🙂) and decided that this would be an interesting topic for analysis.</p>
            
            ---
            # Quick Navigation
            - <p>If you want to know where I got the data from, go here <a href = "http://localhost:8501/Data%20Collection" target='_self'>here</a></p>
            - <p>Which one out of Mess 1 and Mess 2 has a higher overall rating?</p>
            - <p>What is the frequency of the conducted polls?</p>
            - <p>How does the day and time affect ratings?</p>
            - <p>What was the impact of tender changes (if any)?</p>
            
            """,unsafe_allow_html=True)

# I wanted to focus on a dataset that’s personally relevant and impactful for our community. Instead of analyzing a random dataset from the internet, I wanted to engage with something that reflects our daily experiences and offers actionable insights.