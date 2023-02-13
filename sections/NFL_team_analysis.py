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

st.title('NFL play-by-play analysis')


# In[20]:


st.markdown('**The National Football League (NFL)** is the largest professional football league in the United States. The NFL takes the legal form of a sports association, controlled by its own members [1](https://es.wikipedia.org/wiki/National_Football_League).')

st.markdown('The NFL currently consists of 32 franchises based in various US cities and regions. It is divided into two conferences: the National Football Conference (NFC) and the American Football Conference (AFC). In turn, each conference is made up of four divisions (North, South, East and West) and each division is made up of four teams.')

st.markdown('The regular season consists of an 18-week schedule during which each team has a bye week, meaning that the team does not play in that week, consisting of six games against opponents in the same division (there are 8 divisions of 4 teams each). Each team has several inter-divisional and inter-conference duels. It starts on the Thursday night of the first full week of September (the Thursday after Labor Day) and continues until early January. At the end, seven teams - the four division champions and three wild cards - from each conference play in the playoffs. After that, its on to the conference finals, where the winning conference champions go straight to the dream game known as the Super Bowl.')


st.markdown('The intention of this analysis is to provide information about how the NFL considering metrics such as:') 
st.write('- Completions')
st.write('- Attempts')
st.write('- Interceptions')
st.write('- Touchdowns')
st.write('- Turnovers')
st.write('- Passes and rushes')
st.write('- Rushing and passing yards')
st.write('')


# In[10]:

#df = nfl.import_pbp_data([2018,2019,2020,2021,2022], downcast=True, cache=False, alt_path=None)



# In[25]:


df=nfl.import_weekly_data([2022])


# In[19]:


# In[22]:

st.subheader('NFL team analysis')
st.write('The first part of this app analyzes the teamal analysis of the NFL over the past 5 years.')
st.write('The metrics to be analyzed from there are:')
st.write('- Completions by team')
st.write('- Attempts by team')
st.write('- Interceptions by team')
st.write('- Passes done by team')
st.write('- Rushes completed by team')
st.write('- Rushing vs passing yards by team')
st.write('')

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Bar(x=df['recent_team'],
                y=df['completions'],
                name='# completions',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))

fig1.update_layout(
    title='Completions done',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)

fig11 = make_subplots(specs=[[{"secondary_y": True}]])

fig11.add_trace(go.Bar(x=df['recent_team'],
                y=df['attempts'],
                name='# attempts',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))

fig11.update_layout(
    title='Attempts done',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Line(x=df['recent_team'],
                y=df['interceptions'],
                name='# interceptions',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Line(x=df['recent_team'],
                y=df['sacks'],
                name='# sacks',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig2.update_layout(
    title='Interceptions vs sacks by team',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)



st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
st.plotly_chart(fig11, theme="streamlit", use_container_width=True)
st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

col1,col2=st.columns(2)
with col1:
    st.altair_chart(alt.Chart(df)
    .mark_line()
    .encode(x='recent_team:N', y='interceptions:Q',color='recent_team')
    .properties(title='Completed interceptions by team'))

col2.altair_chart(alt.Chart(df)
    .mark_line()
    .encode(x='recent_team:N', y='receptions:Q',color='recent_team')
    .properties(title='Completed receptions by team'))


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Line(x=df['recent_team'],
                y=df['rushing_yards'],
                name='Rushing yards',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Line(x=df['recent_team'],
                y=df['passing_yards'],
                name='Passing yards',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y'))
fig2.add_trace(go.Line(x=df['recent_team'],
                y=df['receiving_yards'],
                name='Receiving yards',
                marker_color='rgb(203, 249, 163)'
                , yaxis='y2'))
fig2.add_trace(go.Line(x=df['recent_team'],
                y=df['sack_yards'],
                name='Sack yards',
                marker_color='rgb(154, 11, 78)'
                , yaxis='y2'))

fig2.update_layout(
    title='Distribution of yards by team and type',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
# Set y-axes titles
fig2.update_yaxes(title_text="Rushing and Passing yards", secondary_y=False)
fig2.update_yaxes(title_text="Receiving and Sack yards", secondary_y=True)

st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Line(x=df['recent_team'],
                y=df['fantasy_points'],
                name='Points',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))

fig2.update_layout(
    title='Fantasy points by team',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)



st.plotly_chart(fig2, theme="streamlit", use_container_width=True)



st.write('')
st.markdown('This app has been done by **_Adrià Parcerisas_**, a PhD Biomedical Engineer related to Machine Learning and Artificial intelligence technical projects for data analysis and research, as well as dive deep on-chain data analysis about cryptocurrency projects. You can find me on [Twitter](https://twitter.com/adriaparcerisas)')
st.write('')
st.markdown('The full sources used to develop this app can be found to the following link: [Github link](https://github.com/adriaparcerisas/NFL)')
st.markdown('_Powered by [Flipside Crypto](https://flipsidecrypto.xyz) and [MetricsDAO](https://metricsdao.notion.site)_')


# In[ ]:




