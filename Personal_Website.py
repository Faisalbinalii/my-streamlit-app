
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
import requests
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt

#
def load_Lot(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_analyst = load_Lot("https://lottie.host/25213c41-9313-4bd8-8e86-6ee7fdad5ca2/7z7kYRBJXf.json")
#

# Page configuration
st.set_page_config(page_title="Faisal Alamri - Personal Website", page_icon=":male-technologist:", layout="wide")

# Custom Layout
st.title("Faisal's **Personal Website**", anchor=None)
st.write("##")
st.write("##")

#option_menu
with st.container():
         selected = option_menu(
             menu_title = None,
             options = ['ME','Projects',"Contact me"],
             icons = ['file-person', 'file-binary' , 'envelope'],
             orientation='horizontal'
             )
if selected == 'ME':
         with st.container():
            col1 , col2 = st.columns(2)
            with col1:
                st.write("##")
                st.subheader("I am Faisal")
                st.title("**Data Analyst at** DataPlus")
            with col2:
                st.lottie(lottie_analyst)
         st.write("---")
         with st.container():
            col3, col4 = st.columns(2)
            with col3:
                st.subheader("""
                Experince
                - Data Analys & BI at DataPlus
                """)
                
              
            with col4:               
                st.subheader("""
                Education
                - Prince Sattam bin tAbeulaziz University (PSAU)
                - Bachelor's of Computer Scinces
                - 3.99 / 5.00 GPA
                - Graduate at DEC 2023
                """)
