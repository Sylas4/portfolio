import streamlit as st
from PIL import Image
import time
import streamlit.components.v1 as components

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import random

st.set_page_config(page_icon="🗂", layout="wide", page_title = "Lilian Martin", initial_sidebar_state = "auto")
# 📰 

list = [{"A":1, "B":2, "C":3},
        {"A":4, "B":5, "C":6},
        {"A":7, "B":8, "C":9}]
def get_answer():
    return random.choice(list)

pa = st.button("Play again")

if 'answer' not in st.session_state.keys() or pa:
    st.session_state['answer'] = get_answer()
    st.session_state['myans'] = "Let me guess.."

st.session_state['country'] = st.session_state['answer']["B"]

if st.session_state['myans'] == st.session_state['answer']:
    st.session_state['right'] = True
else:
    st.session_state['right'] = False

# def show_answer(myans):
#     if myans == st.session_state.answer:
#         return "Horray !"
st.session_state

st.text_input("Lequel ?", st.session_state['myans'], key="myans")


if st.session_state["right"]:
    st.write("Horray !", st.session_state['answer'])







tab1, tab2, tab3 = st.tabs(['tab1', 'tab2', 'tab3'])
with tab1:
    colA,colB,colC = st.columns(3)
    with colA:
        st.write("ok")
    with colB:
        st.write("ok")
    with colC:
        st.write("ok")
with tab2:
    colA,colB,colC = st.columns(3)
    with colA:
        st.write("ok")
    with colB:
        st.write("ok")
    with colC:
        st.write("ok")
    
with tab3:
    colA,colB,colC = st.columns(3)
    with colA:
        st.write("ok")
    with colB:
        st.write("ok")
    with colC:
        st.write("ok")


# ##### Projects ######
# st.markdown('''
# # My Data projects
# ''')
# #####################
# st.markdown('''
# # Assurancetourix

# Projet visant à déployer un modèle de machine learning permettant de prédire le coup d'assurance santé d'une personne en fonction de critères divers.

# ''')
# st.info('''
# - widgets streamlit
# - pickle
# - prediction
# - Explicabilité avec SHAP
# ''')

# #####################
# st.markdown('''
# # Plot your func

# Projet visant à déployer un modèle de machine learning permettant de prédire le coup d'assurance santé d'une personne en fonction de critères divers.

# ''')

# #####################
# st.markdown('''
# # La loi dé grands nombres

# ''')

# #####################
# st.markdown('''
# # Statistiques inférentielles

# ''')


