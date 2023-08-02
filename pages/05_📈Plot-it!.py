import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from numpy import cos, sin, tan, sqrt, log
import plotly.graph_objects as go
import numpy as np


st.set_page_config(page_icon="📈", page_title = "Lilian Martin",
                   initial_sidebar_state = "auto", layout="wide")

with open("./styles/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.markdown('''# Plot-it
The idea behind this little application was to have on hand a solution that would allow me to show the look of different functions.
            
Coming soon: the ability to enter the function of your choice by hand.''')

# available functions list
functions = ['x**2', 'x**3', 'x**.5', 'log(x)', '1/x', 'cos(x)', 'tan(x)', 'sin(x)']

# Sidebar
with st.sidebar:
     options = st.multiselect(
          '**Which functions do you want to plot ?**',
          functions, ['cos(x)', 'tan(x)', 'sin(x)'])

     st.markdown("**Define axis limits**")

     col1, col2 = st.columns([1,1])
     with col1:
          xmin = st.number_input("xmin", value=-10)
          ymin = st.number_input("ymin", value=-10)

     with col2:
          xmax = st.number_input("xmax", value=10)
          ymax = st.number_input("ymax", value=10)

# The plot :
x = np.arange(xmin, xmax, .1)
fig = go.Figure()

for i in functions:
     if i in options:
          y=eval(i)
          if i=='tan(x)':
               y[:-1][np.diff(y) < 0] = np.nan
          fig.add_trace(
               go.Scatter(x=x, y=y, name=i, line_shape='spline',
                          line=dict(width=3)))

#fig.update_traces(hoverinfo='text+name')
fig.update_layout(legend=dict(y=0.5, traceorder='reversed', font_size=16), 
yaxis_range=[ymin, ymax], height=600)

st.plotly_chart(fig, use_container_width=True)
