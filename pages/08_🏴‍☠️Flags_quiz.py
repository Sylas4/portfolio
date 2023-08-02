import streamlit as st
from PIL import Image
import numpy as np
from io import BytesIO
import requests
from fuzzywuzzy import fuzz

st.set_page_config(page_icon="🏴‍☠️", page_title = "Lilian Martin",
                   layout="wide", initial_sidebar_state = "auto")

with open("./styles/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

colA, colB = st.columns([3,1])
with colA:
    st.markdown('''# Are you a good pirate?
Find out which country the flag belongs to. <br>
Don't forget to press "Enter" to validate your answer. <br>
You can try as many times as you like, and spelling mistakes are corrected automatically.''',
unsafe_allow_html=True)

with colB:
    st.image(Image.open('./img/strawhat.jpeg'))

# récupérer le json avec tous les countries
@st.cache_data
def countries():
  json = requests.get("https://restcountries.com/v3.1/all").json()
  return json

# récupérer un id country.
def get_id():
    return np.random.randint(0,249)

# récupérer un flag
def showflag(id, s=1):
    url = countries_json[id]['flags']['png']
    return st.image(Image.open(BytesIO(requests.get(url).content)))

# récupérer le nom du pays.
def showcountry(id):
    return countries_json[id]['name']['common']

def tryagain():
    st.session_state['tryagain'] = True


countries_json = countries()

pa = st.button("Play again")
##########################################
if 'id' not in st.session_state or pa:
    st.session_state['id'] = get_id()
if 'tryagain' not in st.session_state or pa:
    st.session_state['tryagain'] = False
if 'answer' not in st.session_state or pa:
    st.session_state['answer'] = "Let me guess.."

st.session_state['country'] = showcountry(st.session_state['id'])
st.session_state['right'] = fuzz.token_sort_ratio(st.session_state['answer'], st.session_state['country']) >= 80

# st.write(fuzz.token_sort_ratio(st.session_state['answer'], 
#                                st.session_state['country']))
# st.session_state

showflag(st.session_state['id']) 

st.text_input("**What flag is that? Don't worry if the spelling isn't perfect, I'll understand**",
              st.session_state['answer'], key='answer', on_change=tryagain)

if st.session_state["right"]:
    st.markdown(f'''**Horray ! The correct answer is :**
                #### {st.session_state['country']}''')

elif st.session_state["tryagain"]: 
    st.markdown("**Don't give up! You can try again !**")
    answer = st.button("Je donne ma langue au chat (French expression)")
    if answer:
        st.markdown(f'''**The answer was: {st.session_state['country']}**''')
        
