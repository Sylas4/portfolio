import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
from functions import dashboard   

st.set_page_config(page_icon="🌍", page_title = "Lilian Martin", layout="wide", initial_sidebar_state="auto")

with open("./styles/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

##### LOAD DATA ########################################

demodf = dashboard.demo_df()
df = dashboard.merged_df()
img = dashboard.get_img()
indicators = list(set(demodf["Indicator Name"]))

##### SIDE BAR #########################################

# On choisi nos colonnes et leur échelle (logarithmique ou non)
with st.sidebar:
    with st.expander("**Click here's for explanations**"):
        st.markdown('''
        #### Here's how it work
        This dashboard represents each country depending on two indicators plus its population, and then animate the evolution of these indicators over the year.
        These indicators are economic, social or demographic and can be selected
        from the sidebar:
        - CO2 emissions
        - Electricity consumption
        - Energy consumption (in oil)
        - Share of exports in GDP
        - Fertility rate
        - Evolution of GDP
        - Share of imports in GDP
        - Share of industry in GDP
        - Services as a percentage of GDP
        - Share of loans to individuals of GDP
        - Share of agriculture in GDP
        - Life expectancy at birth
        - Population densitys
        ''') 
    st.markdown('''**Choose two indicators to compare**
    ''')
    X = st.sidebar.selectbox(
        "Pick the X column",
        indicators,
        index = indicators.index("Life expectancy at birth, total (years)")
    )
    logx = st.checkbox("Log scale", key="X")

    Y = st.sidebar.selectbox(
        "Now, choose Y column",
        indicators,
        index = indicators.index("Fertility rate, total (births per woman)")
    )
    logy = st.checkbox("Log scale", key="Y")


########################################################
##### X & Y RANGES #####################################
########################################################

# On leur ajoute un peu de valeur pour que les bulles ne soient pas trop cropped

xbinf = min(df[X].dropna()) - min(df[X].dropna())/10
xbsup = max(df[X].dropna()) + max(df[X].dropna())/10
ybinf = min(df[Y].dropna()) - min(df[Y].dropna())/10
ybsup = max(df[Y].dropna()) + max(df[Y].dropna())/10

########################################################
##### PLOTLY ###########################################
########################################################

fig = px.scatter(df, 
    x=X, 
    y=Y, 
    size = "pop",
    color ="continent",
    hover_name='country',
    animation_frame="year", 
    animation_group="country",
    size_max=100,
    # title = "{} vs {}".format(X,Y),
    # hover_data=["continent",X,Y],
    height = 750,
    log_x=logx,
    log_y=logy,
    range_x=[xbinf,xbsup], 
    range_y=[ybinf,ybsup]
    )

fig.update_layout(legend=dict(
    orientation="h",
    yanchor="top",
    y=1,
    xanchor="right",
    x=1),
    title=dict(
        text="{} vs {}".format(X,Y),
        font=dict(size=20))
)

########################################################
##### ON DISPOSE NOS ELEMENTS EN DEUX COLONNES #########
########################################################

col1, col2 = st.columns([4,1])


st.markdown('''# Demography animation 
*'Jusqu'à ce qu'elle m'aime, la France, je vais la démographier'* - Médine''')
st.plotly_chart(fig, use_container_width=True)





        



