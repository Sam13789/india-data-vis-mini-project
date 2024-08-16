import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
india = pd.read_csv('india.csv')

list_of_states = india['State'].unique().tolist()
list_of_states.insert(0, 'Overall India')

st.sidebar.title('India Data Analysis')
selected_state = st.sidebar.selectbox('Select a State', list_of_states)
st.sidebar.title('Select Basis Of Analysis')
primary = st.sidebar.selectbox('Primary Factor', india.columns[5:].tolist())
secondary = st.sidebar.selectbox('Secondary Factor', india.columns[5:].tolist())
plot = st.sidebar.button('Plot Graph')
if plot:
    st.text('Size represents primary factor')
    st.text('Color represents secondary factor')
    if selected_state == 'Overall India':
        # plot for whole india
        fig = px.scatter_mapbox(india, lat="Latitude", lon="Longitude", size=primary, color=secondary,color_continuous_scale='inferno', size_max=35, zoom=3.7,
                                mapbox_style="carto-positron",width=1200,height=700, hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        # plot for state
        state = india[india['State'] == selected_state]
        fig = px.scatter_mapbox(state, lat="Latitude", lon="Longitude", size=primary, color=secondary,
                                color_continuous_scale='inferno', size_max=35, zoom=5.5,
                                mapbox_style="carto-positron", width=1200, height=700, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)