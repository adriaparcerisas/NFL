#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.ticker as ticker
import numpy as np
import plotly.express as px
import altair as alt
import nfl_data_py as nfl

st.title('NFL 2022 season overview')


# In[20]:


st.markdown('**The National Football League (NFL)** is the largest professional football league in the United States. The NFL takes the legal form of a sports association, controlled by its own members [1](https://es.wikipedia.org/wiki/National_Football_League).')

st.markdown('The NFL currently consists of 32 franchises based in various US cities and regions. It is divided into two conferences: the National Football Conference (NFC) and the American Football Conference (AFC). In turn, each conference is made up of four divisions (North, South, East and West) and each division is made up of four teams.')

st.markdown('The regular season consists of an 18-week schedule during which each team has a bye week, meaning that the team does not play in that week, consisting of six games against opponents in the same division (there are 8 divisions of 4 teams each). Each team has several inter-divisional and inter-conference duels. It starts on the Thursday night of the first full week of September (the Thursday after Labor Day) and continues until early January. At the end, seven teams - the four division champions and three wild cards - from each conference play in the playoffs. After that, its on to the conference finals, where the winning conference champions go straight to the dream game known as the Super Bowl.')


st.markdown('The intention of this analysis is to provide information about how the NFL considering metrics such as:')
st.write('- Teams')
st.write('- Players')
st.write('- Positions')
st.write('')
st.write('All of the analysis can be found on the sidebar situated at the left of the page where you can navigate and explore each analysis in a dive deep comparison.')

st.write('')
st.markdown('This app has been done by **_Adrià Parcerisas_**, a PhD Biomedical Engineer related to Machine Learning and Artificial intelligence technical projects for data analysis and research, as well as dive deep on-chain data analysis about cryptocurrency projects. You can find me on [Twitter](https://twitter.com/adriaparcerisas)')
st.write('')
st.markdown('The full sources used to develop this app can be found to the following link: [Github link](https://github.com/adriaparcerisas/NFL)')
st.markdown('_Powered by [Flipside Crypto](https://flipsidecrypto.xyz) and [MetricsDAO](https://metricsdao.notion.site)_')


# In[ ]:
