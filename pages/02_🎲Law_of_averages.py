import streamlit as st
import numpy as np
import time
import altair as alt
import pandas as pd


st.set_page_config(page_icon="🎲", layout="centered", page_title = "Lilian Martin",
                   initial_sidebar_state = "auto")

with open("./styles/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

###############################################################
def animate(n,t, chart):
    for i in range(1, n+1):
        d1 = np.random.randint(1,7)
        d2 = np.random.randint(1,7)
        s = d1+d2
        data.iloc[s-2,1] +=1
        
        chart.altair_chart(c, use_container_width=True) 

        p = i/n*100
        progress_bar.progress(float(i/n))
        status_text.text(f"{round(p)}% Complete")

        time.sleep(t)
###############################################################

st.markdown('''# La loi dé grands nombres ! 
(french bad pun for 'Law of lager numbers')
#### How does chance work? 
The law of large numbers or law of averages simply states that with a sufficiently large sample, the frequency of a random event will be close to its probability.  

Do you know the game "CATAN"? If not, I recommend you play it.
            
For the storytelling, my aunt was questioning the law of probabilities because the resources she'd bet on never came out. So I created this animation to show her that, even though in theory 6, 7 & 8 should come out more, with few rolls of the dice, this wasn't necessarily the case...

I've continued to use this application with my students to popularize the law of large numbers when dealing with inferential statistics. 

##### Choose a number of throws of two 6-sided dice, then observe whether the probabilities are respected, then increase the number of throws!''')

n = st.slider('**How many rolls ?**', key="rolls",
              min_value=5, max_value=100, value=5, step=5)

t = st.radio('''**Speed between animations (seconds)**''', key='time',
             options=(.1, 0.25, .5), index = 1, horizontal = True)
###############################################################

data = pd.DataFrame(list({i: 0 for i in range(2, 13)}.items()), columns=['results', 'freq'])
chart = st.empty()
c = alt.Chart(data).mark_bar(color='#800000', size=50).encode(x='results:O', y='freq:Q')

progress_bar = st.progress(0.0)
p = 0.0
status_text = st.empty()

###############################################################

if st.button("**(re)Start**", key="launch"):
    animate(n,t, chart)

