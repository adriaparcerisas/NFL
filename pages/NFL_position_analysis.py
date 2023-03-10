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

st.title('NFL position analysis')


# In[20]:

st.markdown('The intention of this analysis is to provide information about how each NFL position evolved over this current season considering metrics such as:') 
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

st.subheader('NFL position analysis')
st.write('The first part of this app analyzes the position analysis of the NFL over the current season.')
st.write('The metrics to be analyzed from there are:')
st.write('- Completions by position')
st.write('- Attempts by position')
st.write('- Interceptions by position')
st.write('- Passes done by position')
st.write('- Rushes completed by position')
st.write('- Rushing vs passing yards by position')
st.write('')

import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.altair_chart(alt.Chart(df, width=600)
    .mark_bar()
    .encode(x='sum(completions)', y=alt.Y('position',sort='-x'),color=alt.Color('position', scale=alt.Scale(scheme='dark2')))
    .properties(title='Number of completions by position'))


st.altair_chart(alt.Chart(df, width=600)
    .mark_bar()
    .encode(x='sum(attempts)', y=alt.Y('position',sort='-x'),color=alt.Color('position', scale=alt.Scale(scheme='dark2')))
    .properties(title='Number of attempts by position'))


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Bar(x=df['position'],
                y=df['interceptions'],
                name='# interceptions',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Bar(x=df['position'],
                y=df['sacks'],
                name='# sacks',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig2.update_layout(
    title='Interceptions vs sacks by position',
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

fig1 = px.line(df, x="position", y="interceptions", color="position", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Completed incerceptions by position',
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

fig2 = px.line(df, x="position", y="receptions", color="position", color_discrete_sequence=px.colors.qualitative.Vivid)
fig2.update_layout(
    title='Completed receptions by position',
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

fig2.add_trace(go.Bar(x=df['position'],
                y=df['rushing_yards'],
                name='Rushing yards',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Bar(x=df['position'],
                y=df['passing_yards'],
                name='Passing yards',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y'))
fig2.add_trace(go.Bar(x=df['position'],
                y=df['receiving_yards'],
                name='Receiving yards',
                marker_color='rgb(203, 249, 163)'
                , yaxis='y2'))
fig2.add_trace(go.Bar(x=df['position'],
                y=df['sack_yards'],
                name='Sack yards',
                marker_color='rgb(154, 11, 78)'
                , yaxis='y2'))

fig2.update_layout(
    title='Distribution of yards by position and type',
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

fig1 = px.line(df, x="position", y="fantasy_points", color="position", color_discrete_sequence=px.colors.qualitative.Vivid)
fig1.update_layout(
    title='Fantasy points scored by position',
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
st.markdown('This app has been done by **_Adri?? Parcerisas_**, a PhD Biomedical Engineer related to Machine Learning and Artificial intelligence technical projects for data analysis and research, as well as dive deep on-chain data analysis about cryptocurrency projects. You can find me on [Twitter](https://twitter.com/adriaparcerisas)')
st.write('')
st.markdown('The full sources used to develop this app can be found to the following link: [Github link](https://github.com/adriaparcerisas/NFL)')
st.markdown('_Powered by [Flipside Crypto](https://flipsidecrypto.xyz) and [MetricsDAO](https://metricsdao.notion.site)_')


# In[ ]:




