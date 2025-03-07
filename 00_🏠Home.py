import streamlit as st
from PIL import Image
from functions import layout
from matplotlib import pyplot as plt
    
#st.set_page_config(layout="wide", page_title="Interactive table app")
# 📰 
st.set_page_config(page_icon="🈺", layout="wide", page_title = "Lilian Martin", initial_sidebar_state = "auto")

with open("./styles/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

###### Header ######
col1, col2 = st.columns([3,1])
with col1:
    st.markdown('# Martin Lilian, Data scientist')
    st.markdown('''Welcome to my portfolio! <br>
                Here you'll find a collection of my data science projects that showcase my skills and passion for analytics, visualization, scraping and machine learning. I'll be adding more projects soon, so stay tuned. <br>
                In the meantime, feel free to contact me if you have any questions or would like to discuss potential collaborations.''',
                unsafe_allow_html=True)
with col2:
    st.image(Image.open('img/pp_2.jpeg'))

col1, col2 = st.columns([3,1])
with col1:
    st.success('''
        Dynamic, disciplined & determined, I'm keen to put my skills at the service of causes that are dear to me. My favorite missions are scraping, SQL queries and streamlit development.
        - Data scientist with 4 years' experience
        - Python/SQL as primary languages
        - Analytics & Scraping skills
        - Data teacher experience
        ''')
with col2:
    st.markdown('''**[LinkedIn](https://www.linkedin.com/in/lilianmartin4/)
                martin.lilian4@gmail.com**''')
    l = st.radio("Download my resume in FR/ENG:",
        ("ENG","FR"), horizontal=True)
    with open(f"./data/{l}_resume.pdf", "rb") as cv_file:
        cv = cv_file.read()
    st.download_button("Resume", data = cv, file_name=f'Lilian_Martin.pdf',
                       mime="application/octet-stream")


###### Hard Skills ######
st.markdown('''
# Hard Skills
''')
layout.txt3('Programming', '`Python`, `VBA`, `SAS`')
layout.txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
layout.txt3('SGBD', '`MySQL`, `PostgreSQL`, `SQLite`')
layout.txt3('Scraping', '`BeautifulSoup`, `Scrapy`')
layout.txt3('Data visualization', '`matplotlib`, `plotly`, `seaborn`')
layout.txt3('Business Intelligence', '`AWS Quicksight`, `Looker Studio`, `Tableau`, `Qlik`')
layout.txt3('Machine Learning', '`scikit-learn`')
layout.txt3('Deep Learning', '`tensorflow-keras`')
layout.txt3('Model deployment', '`streamlit`, `Flask`, `Dash`')
layout.txt3('ChatGPT', '`prompt engineering`, `OpenAI API`')

###### Skills ######
st.markdown('''
# Skills
''')
layout.txt3('**Speaking**', 'At ease in speaking, pedagogue, patient, good communicator, able to pass on knowledge and popularize.')
layout.txt3('**Emotional intelligence**', 'Ease of understanding others and adapting to my audience')
layout.txt3('**Good executive**', 'Adaptable, multidisciplinary, resilient')

###### Work Experience ######
st.markdown('# Work Experience')

###### VIAPLAY ######
layout.txt('''### Data scientist''',
'<h5 class=years>Current role</h5>')
col1, col2 = st.columns([3,2])
with col1:
    st.markdown('''
    **Viaplay Group, Stockholm**
    - Developed a Data Quality Index to maintain high standards in our event tracking system.
    - Analyzed customer behavior data to enhance the user experience, evaluate new features, and monitor errors.
    - Developed dashboards using Tableau, Databricks, SQL, pyspark, and AWS Quicksight to streamline information.
    - Collaborated with a team of data scientists, data engineers, developers, and product owners to drive project success.
    ''')
# with col2:
#     st.image(Image.open('img/tf1_2.png'))
st.markdown('---')

layout.txt('''### Data scientist / Training Manager''',
'<h5 class=years>2021 - 2023</h5>')

col1, col2 = st.columns([3,2])
with col1:
    st.markdown('''
    **Matrice, Paris**
    - Training design & implementation
    - Training on Python, SQL, Looker...
    - Data analysis, machine learning, scraping...
    - 50 data analysts trained on-site
    - Coaching in professional reintegration
    - Reference : tjohnson@matrice.io |  pflouvat@matrice.io | s.olivera.silvera@gmail.com
    ''')
with col2:
    st.image(Image.open('img/tf1_2.png'))

st.markdown('---')

###### Rise Up #######
layout.txt('''### Data analyst''',
'<h5 class=years>2021 - 2023</h5>')

col1, col2 = st.columns([3,2])
with col1:
    st.markdown('''
    **Rise Up, Paris**
    - Creation of a datalab for our customers
    - Business Intelligence: dashboards realization (`AWS Quicksight` & `MySQL`)
    - Communication with customers
    - Reference : guillaume@riseup.ai
    ''')
with col2:
    st.image(Image.open('img/tf1_1.png'))
st.markdown('---')

###### SCCF #######
layout.txt('### Statistical Studies Officer',
'<h5 class=years>2018 - 2019</h5>')

col1, col2 = st.columns([3,2])
with col1:
    st.markdown('''
    **Secours Catholique Caritas France, Paris**
    - Participation in two statistical reports, State of poverty in France (2018 & 2019)
    - Use of VBA, SAS & Excel to clean up, analyze and model the data required for the statistical report.
    
    **Volunteer**
    - Organization of events with the beneficiaries of the association. 
    - Animation of a soccer tournament at Clairefontaine (training center of the French national soccer team).
    ''')
with col2:
    st.image(Image.open('./img/sccf.png'), width=250)
st.markdown('---')


###### Other jobs ######
layout.txt('#### Lead Bartender',
'<h5 class=years>2019 - 2022</h5>')

st.markdown('''
    **La base, Paris, volunteer**
    - Bar tending
    - Events management
    - Communication
    - Marauding
    - Mentoring
''')     
st.markdown('---')
# 

layout.txt('##### Census officer, INSEE/Mairie du 13e, Paris',
'<h5 class=years>2018</h5>')
# 

layout.txt('##### Investigator, ORIVE, Paris',
'<h5 class=years>2017 - 2018</h5>')
# 

layout.txt('##### BAFA animator, Enfants du métro, Paris',
'<h5 class=years>2015 - 2018</h5>')
st.markdown('''- Caring for children in summer camp
''')
# 

layout.txt('##### Odd jobs, Adecco, Paris',
'<h5 class=years>2013-2014</h5>')
st.markdown('---')

###### Education ######
st.markdown('''
# Education
''')

###### Open Classrooms ######
layout.txt('### Data Analyst | OpenClassrooms X ENSAE-ENSAI', 
'<h5 class=years>2019-2021</h5>')
st.markdown('''
- Data analysis, machine learning
- Learned `Python3` & `MySQL`
- Data scraping
- 10 professional projects. 
- A final statiscal report on `UFC`
- Reference: romainwarlop@gmail.com
''')
st.markdown('---')
# 

###### Demography ######
layout.txt("### Demography | Paris 1 Panthéon-Sorbonne | Master's degree", 
'<h5 class=years>2014-2019</h5>')
st.markdown(''' - Training in sociology & statistics''')

#####################
st.markdown('''
## Hobbies
''')
layout.txt2('🤼', '**Martial arts**', 'MMA, BJJ, Karate')
layout.txt2('🏂', '**Others sports**', 'Longboard, snowboard')
layout.txt2('🥊', '**Watching combat sports compétition**', 'UFC, Cage warriors, PFL, KSW, ADCC')
layout.txt2('🕹', '**E-sport**', 'League of Legend, (Fnatic fanboy)')
layout.txt2('🦾','**Mangas**', 'FMA, AOT, Gangsta')
layout.txt2('🗣', '**Art**', 'Theater, public speech, graphic art')
layout.txt2('🚂','**Solo travelling**', 'Scandinavia')
layout.txt2('🍻','**Volunteering**', 'Bar tending')


