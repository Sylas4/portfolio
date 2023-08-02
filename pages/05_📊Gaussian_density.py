import streamlit as st
import matplotlib.pyplot as plt
from functions import gaussienne as gauss

st.set_page_config(page_icon="🈺", page_title = "Mon streamlit", layout="wide")

st.markdown("# Display the probability density function")
st.markdown('''
This application allows you to visualize what the p-value represents in terms of the area of the Gaussian distribution.

Conversely, it can also be used to visualize which T-value corresponds to a given p-value, in a one or two-tailed situation.

This is a very useful app for popularizing inferential statistics and understanding the difference between a one-tailed and two-tailed hypothesis.
''')

plt.style.use('seaborn-whitegrid') # grid

# Si unilatéral on fait un slider pour Z de -3.5 à 3.5
Z = st.sidebar.slider('Score Z',(-3.5),3.5,.0, key="Z")
std = st.sidebar.slider('Std',0.5,3.0,1.0, step=0.1, key="std")
A = st.sidebar.slider('Aire',0.0,.99,0.95, key="a")

# On défini une box de sélection avec le choix Unilatéral ou Bilatéral
option = st.sidebar.selectbox('Unilateral or Bilateral',('Unilateral','Bilateral'))

layout = st.sidebar.columns([1,1])

with layout[0]:
    ba = st.button("Find the area corresponding to the Z score.")
        # Si unilatéral on utilise le fonction plot_unilatéral_z

with layout[1]:
    bb = st.button("Find the Z score corresponding to the area")
        # Si unilatéral on utilise le fonction plot_unilatéral

if ba == True and option == "Unilateral":
    st.pyplot(gauss.plot_unilateral_z(Z,std))
elif ba == True and option == "Bilateral":
    st.pyplot(gauss.plot_bilateral_z(Z,std))
elif bb == True and option == "Unilateral":
    st.pyplot(gauss.plot_unilateral(A,std))
elif bb == True and option == "Bilateral":
    st.pyplot(gauss.plot_bilateral(A,std))

