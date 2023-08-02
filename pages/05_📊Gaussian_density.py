import streamlit as st
import matplotlib.pyplot as plt
from functions import gaussienne as gauss

st.set_page_config(page_icon="🈺", page_title = "Mon streamlit", layout="wide")

st.markdown("# Display the probability density function")
st.markdown('\n')
st.markdown("""
Cette application permer de visualiser l'aire sous courbe (ou p-value) pour un nombre Z d'écart-type. \n
A l'inverse, elle permet aussi de visualiser quel score Z correspond à une aire sous courbe donnée, dans une situation uni ou bilatérale. \n
""")

plt.style.use('seaborn-whitegrid') # grid

# Si unilatéral on fait un slider pour Z de -3.5 à 3.5
Z = st.sidebar.slider('Score Z',(-3.5),3.5,.0, key="Z")
std = st.sidebar.slider('Std',0.5,3.0,1.0, step=0.1, key="std")
A = st.sidebar.slider('Aire',0.0,.99,0.95, key="a")

# On défini une box de sélection avec le choix Unilatéral ou Bilatéral
option = st.sidebar.selectbox('Selectioner Unilatéral ou Bilatéral',('Unilatéral','Bilatéral'))

layout = st.sidebar.columns([1,1])

with layout[0]:
    ba = st.button("Trouvez l'aire correspondant au score Z")
        # Si unilatéral on utilise le fonction plot_unilatéral_z

with layout[1]:
    bb = st.button("Trouvez le score Z correspondant à l'aire")
        # Si unilatéral on utilise le fonction plot_unilatéral

if ba == True and option == "Unilatéral":
    st.pyplot(gauss.plot_unilateral_z(Z,std))
elif ba == True and option == "Bilatéral":
    st.pyplot(gauss.plot_bilateral_z(Z,std))
elif bb == True and option == "Unilatéral":
    st.pyplot(gauss.plot_unilateral(A,std))
elif bb == True and option == "Bilatéral":
    st.pyplot(gauss.plot_bilateral(A,std))

