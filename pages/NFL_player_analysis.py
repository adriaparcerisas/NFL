#!/usr/bin/env python
# coding: utf-8

# In[2]:


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

st.title('NFL player analysis')


# In[20]:

st.markdown('The intention of this analysis is to provide information about how each NFL player evolved over this current season considering metrics such as:') 
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



# In[3]:


df=nfl.import_weekly_data([2022])


# In[4]:


df


# In[5]:


# In[22]:

st.subheader('NFL player analysis')
st.write('The first part of this app analyzes the player analysis of the NFL over the current season.')
st.write('The metrics to be analyzed from there are:')
st.write('- Completions by player')
st.write('- Attempts by player')
st.write('- Interceptions by player')
st.write('- Passes done by player')
st.write('- Rushes completed by player')
st.write('- Rushing vs passing yards by player')
st.write('')

import plotly.graph_objects as go
from plotly.subplots import make_subplots

chart=alt.Chart(
    source,
).mark_bar().encode(
    x=alt.X('player_name:N', sort='-y'),
    y='sum(completions)',
    color=alt.Color('player_name:Q')

).transform_window(
    rank='rank(sum(completions))',
    sort=[alt.SortField('sum(completions)', order='descending')]
).transform_filter(
    (alt.datum.rank < 10)
)
st.altair_chart(chart, theme="streamlit", use_container_width=True)


st.altair_chart(alt.Chart(df, width=600)
    .mark_bar()
    .encode(x='sum(attempts)', y=alt.Y('player_name',sort='-x'),color=alt.Color('player_name', scale=alt.Scale(scheme='dark2')))
    .properties(title='Number of attempts by player'))


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Bar(x=df['player_name'],
                y=df['interceptions'],
                name='# interceptions',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Bar(x=df['player_name'],
                y=df['sacks'],
                name='# sacks',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig2.update_layout(
    title='Interceptions vs sacks by player',
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

fig1 = px.line(df, x="player_name", y="interceptions", color="player_name", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Completed incerceptions by player',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

fig2 = px.line(df, x="player_name", y="receptions", color="player_name", color_discrete_sequence=px.colors.qualitative.Vivid)
fig2.update_layout(
    title='Completed receptions by player',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
st.plotly_chart(fig2, theme="streamlit", use_container_width=True)


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Bar(x=df['player_name'],
                y=df['rushing_yards'],
                name='Rushing yards',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Bar(x=df['player_name'],
                y=df['passing_yards'],
                name='Passing yards',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y'))
fig2.add_trace(go.Bar(x=df['player_name'],
                y=df['receiving_yards'],
                name='Receiving yards',
                marker_color='rgb(203, 249, 163)'
                , yaxis='y2'))
fig2.add_trace(go.Bar(x=df['player_name'],
                y=df['sack_yards'],
                name='Sack yards',
                marker_color='rgb(154, 11, 78)'
                , yaxis='y2'))

fig2.update_layout(
    title='Distribution of yards by player and type',
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

fig1 = px.line(df, x="player_name", y="fantasy_points", color="player_name", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Fantasy points scored by player',
    xaxis_tickfont_size=14,
    yaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
st.plotly_chart(fig1, theme="streamlit", use_container_width=True)


st.write('')
st.markdown('This app has been done by **_Adrià Parcerisas_**, a PhD Biomedical Engineer related to Machine Learning and Artificial intelligence technical projects for data analysis and research, as well as dive deep on-chain data analysis about cryptocurrency projects. You can find me on [Twitter](https://twitter.com/adriaparcerisas)')
st.write('')
st.markdown('The full sources used to develop this app can be found to the following link: [Github link](https://github.com/adriaparcerisas/NFL)')
st.markdown('_Powered by [Flipside Crypto](https://flipsidecrypto.xyz) and [MetricsDAO](https://metricsdao.notion.site)_')


# In[ ]:




