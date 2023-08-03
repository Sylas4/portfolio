import streamlit as st
import matplotlib.pyplot as plt
from functions import gaussienne as gauss

st.set_page_config(page_icon="🈺", page_title = "Lilian Martin", layout="wide")

with open("./styles/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.markdown("# Display the probability density function")
st.markdown('''
This application allows you to visualize what the p-value represents in terms of the area of the Gaussian distribution.

Conversely, it can also be used to visualize which T-value corresponds to a given p-value, in a one or two-tailed situation.

This is a very useful app for popularizing inferential statistics and understanding the difference between a one-tailed and two-tailed hypothesis.
''')

plt.style.use('seaborn-whitegrid') # grid

with st.sidebar:
    # On défini une box de sélection avec le choix Unilatéral ou Bilatéral
    option = st.selectbox('Unilateral or Bilateral',('Unilateral','Bilateral'))
    
    # Si unilatéral on fait un slider pour Z de -3.5 à 3.5
    Z = st.slider('Z score',(-3.5),3.5,.0, key="Z")
    std = st.slider('Standard deviation',0.5,3.0,1.0, step=0.1, key="std")
    A = st.slider('Area',0.0,.99,0.95, key="a")

colarea, colz = st.columns([1,1])
with colarea:
    ba = st.button("Find the p-value")
        # Si unilatéral on utilise le fonction plot_unilatéral_zs
with colz:
    bb = st.button("Find the Z-score")
        # Si unilatéral on utilise le fonction plot_unilatéral

if ba and option == "Unilateral":
    st.pyplot(gauss.plot_unilateral_z(Z,std))
elif ba and option == "Bilateral":
    st.pyplot(gauss.plot_bilateral_z(Z,std))
elif bb and option == "Unilateral":
    st.pyplot(gauss.plot_unilateral(A,std))
elif bb and option == "Bilateral":
    st.pyplot(gauss.plot_bilateral(A,std))

