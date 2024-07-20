import streamlit as st
from PIL import Image

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

food_bg = Image.open("./images/food_final.png")
st.image(food_bg)

st.markdown("""
<style>
p {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
            # Overview
            <p>Mess is a crucial aspect of college life, significantly impacting student satisfaction and well-being. To better understand this, I'm conducting a <em><b>mess review analysis</b></em> using data collected from polls conducted by the mess committee of IIITDMJ itself. The aim of this analysis to gain some interesting insights and discover patterns that can help improve the overall dining experience.</p>
            
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
            <p>For this project, I wanted to work on some dataset that was actually relevant to me and our college community, and not some random house price prediction dataset off off kaggle. After <del>a lot of</del> some brainstorming, I stumbled across polls that were conducted by the mess committee on WhatsApp (just goes to show that data is <em>everywhere</em> around you, you just have to look for it 🙂) and decided that this would be an interesting topic for analysis.</p>
            
            ---
            # Quick Navigation
            - <p>If you want to know where I got the data from, go here <a href = "http://localhost:8501/Data%20Collection" target='_self'>here</a></p>
            - <p>Which one out of Mess 1 and Mess 2 has a higher overall rating?</p>
            - <p>What is the frequency of the conducted polls?</p>
            - <p>How does the day and time affect ratings?</p>
            - <p>What was the impact of tender changes (if any)?</p>
            
            """,unsafe_allow_html=True)
