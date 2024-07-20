import streamlit as st
from st_pages import add_page_title
import pandas as pd

st.set_page_config(layout="wide")

mess = pd.read_csv("data/mess_data.csv")
add_page_title()

st.markdown("""
<style>
p {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
            # Sources
            All of the data has been collected from the polls conducted by the mess committee in the following WhatsApp groups:
            
            - <p>Central mess feedback (2023 batch): Data from 11-09-2023 to 17-01-2024</p>
            - <p>Central Mess Feedback: Data from 21-01-2024 to 03-05-2024</p>
            
            ---
            # Process
            As far as I know, there is no simple way to convert WhatsApp poll data into plain text. There's <a href="https://chromewebstore.google.com/detail/export-whatsapp-surveys/engdhlnghkdaoccckbbglafcanmpohob">this</a> chrome extension, but it only exports a single poll at a time. After a lot of searches that lead to no answers, I finally accepted the fact that I would have to type them manually... Yup. So I <em>manually typed 300+ samples</em> into an excel file and exported them as a csv file.
            
            ---
            # Result
            Finally, we have the following dataset:
            
            """, unsafe_allow_html=True)

st.dataframe(mess,use_container_width=True)

st.info("""***Tasty Tidbits***\n\nInitially I had thought of including a column for the dishes that was on the menu, but the menu keeps changing every couple months so there wasn't sufficient data to analyze each dish... I had to drop that idea :(""",icon="💡")